import cadquery as cq
from buttonboxdefs import *
import standoffs

thickness = 10

# ESP
holes_dx = 0.85 * 25.4

# esp standoff dimensions
standoff_h = 5
standoff_d = 7

esp_x_offset = 0
esp_y_offset = 17

standoff = standoffs.round_standoff(standoff_d, standoff_h)

screwpost_d = 10.1 # must be > 2*fillet_r
screwpost = standoffs.square_screwpost_body(screwpost_d, thickness-th, fillet_r)

centerXY = (True, True, False)

# make shell
shell = (cq.Workplane("XY")
         .box(width, length, thickness, centered=centerXY)
         .faces(">Z")
         .shell(-th)
         # round edges
          .edges("<Z or |Z").fillet(fillet_r)
         )
shell.faces("<Z").workplane(centerOption="CenterOfMass", 
                            invert=True).tag("bottom")

# distribute standoffs
standoffs1 = (shell
             .workplaneFromTagged("bottom")
             # place standoffs on bottom
             .transformed(offset=(esp_x_offset, esp_y_offset, th+standoff_h/2))
             .rect(holes_dx, 0, forConstruction=True)
             .vertices()
             .eachpoint(lambda loc: standoff.val().moved(loc), True)
             )
standoffs2 = (shell
             .workplaneFromTagged("bottom")
             # place standoff on bottom
             .transformed(offset=(esp_x_offset, esp_y_offset - 36, th+standoff_h/2))
            .box(17, 4, standoff_h)
             )

# distribute screwposts and holes
screwposts = (shell
              .workplaneFromTagged("bottom")
              .transformed(offset=(0, 0, (th+thickness)/2))
              .rect(width - 1.2*screwpost_d, length - 1.2*screwpost_d, forConstruction=True)
              .vertices()
              .eachpoint(lambda loc: screwpost.val().moved(loc), True)
              )

# combine
result = shell.union(standoffs1).union(standoffs2).union(screwposts)

# screw holes
result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, (th+thickness)/2))
          .rect(width - 1.2*screwpost_d, length - 1.2*screwpost_d, forConstruction=True)
          .vertices()
          .circle(insert_sr+.25)
          .cutThruAll()
          )
result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, 0))
          .rect(width - 1.2*screwpost_d, length - 1.2*screwpost_d, forConstruction=True)
          .vertices()
          .circle(screw_head_r)
          .cutBlind(screw_head_h)
          )

#result = result - opz.esp_jacks_cutter(esp_x_offset, esp_y_offset, th+standoff_h)

show_object(result)
