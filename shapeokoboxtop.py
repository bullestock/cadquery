import cadquery as cq
from shapeokoboxdefs import *

centerXY = (True, True, False)

def square_screwpost_body(d, h, r):
    return (cq.Workplane()
            .box(d, d, h, centered=centerXY)
            .edges("|Z").fillet(r)
            )

screwpost_d = 8
screwpost = square_screwpost_body(screwpost_d, height/2-th, 2)

# make shell
shell = (cq.Workplane("XY")
         .box(width, length, height/2, centered=centerXY)
         .faces(">Z")
         .shell(-th)
         # round edges
         .edges("<Z or |Z").fillet(fillet_r)
         )

shell.faces("<Z").workplane(centerOption="CenterOfMass", 
                            invert=True).tag("bottom")

# distribute screwposts and holes
screwposts = (shell
              .workplaneFromTagged("bottom")
              .transformed(offset=(0, 0, th))
              .rect(width - 1.2*screwpost_d, length - 1.2*screwpost_d, forConstruction=True)
              .vertices()
              .eachpoint(lambda loc: screwpost.val().moved(loc), True)
              )

result = shell.union(screwposts)

result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, height/2))
          .rect(width - 1.2*screwpost_d, length - 1.2*screwpost_d, forConstruction=True)
          .vertices()
          .circle(1.8/2)
          .cutThruAll()
          )

result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, 0))
          .rect(width - 1.2*screwpost_d, length - 1.2*screwpost_d, forConstruction=True)
          .vertices()
          .circle(3.5/2)
          .cutBlind(4)
          )

result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, height/2), rotate=(90, 0, 0))
          .circle(2.45)
          .cutThruAll()
          )

show_object(result)
