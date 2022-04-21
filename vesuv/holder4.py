import cadquery as cq

w = 80
depth = 20
height = 30
bracket_th = 4
d1 = 4.2    
d2 = 8.4

result = (cq.Workplane("XY")
          .box(w, depth, height, centered=(True, True, False))
          .faces("<Z").workplane(centerOption="CenterOfMass", 
                             invert=True).tag("bottom")
          .workplaneFromTagged("bottom")
          # mount plate
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, (depth-bracket_th)/2, -depth))
          .box(w, bracket_th, height, centered=(True, True, False))
          # round edges
          .edges("|Y or <Y").fillet(1)
          # tool holes
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, -depth/6, 0))
          .rarray(w/4, 1, 2, 1)
          .circle(d2/2).cutBlind(25)
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, -depth/5, 0))
          .rarray(w*0.7, 1, 2, 1)
          .circle(d1/2).cutBlind(15)
          # mounting holes
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, -height/2), rotate=(90, 0, 0))
          .rarray(w*0.5, 1, 2, 1)
          .circle(2)
          .cutThruAll()
)

show_object(result)

