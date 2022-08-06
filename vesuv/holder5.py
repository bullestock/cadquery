import cadquery as cq

w = 40
depth = 40
height = 10
bracket_th = 4
d1 = 14

result = (cq.Workplane("XY")
          .box(w, depth, height, centered=(True, True, False))
          .faces("<Z").workplane(centerOption="CenterOfMass", 
                             invert=True).tag("bottom")
          .workplaneFromTagged("bottom")
          # mount plate
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, (depth-bracket_th)/2, -height))
          .box(w, bracket_th, height, centered=(True, True, False))
          # lip
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, (-depth+bracket_th)/2, -3))
          .box(w, bracket_th, 3, centered=(True, True, False))
          # round edges
          .edges("|Y or <Y").fillet(1)
          # tool hole
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, -9, 0))
          .slot2D(30, d1, 90).cutThruAll()
          # mounting holes
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, -height/2), rotate=(90, 0, 0))
          .rarray(w*0.5, 1, 2, 1)
          .circle(2)
          .cutThruAll()
)

show_object(result)

