import cadquery as cq

d1 = 20
d2 = 8.5
depth = 1.25*d1
bracket_th = 4

result = (cq.Workplane("XY")
          .box(3*d1, d1/2, depth, centered=(True, True, False))
          .faces("<Z").workplane(centerOption="CenterOfMass", 
                             invert=True).tag("bottom")
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, 1.25*d1))
          .transformed(rotate=(90, 0, 0))
          .slot2D(2*d1, d1, 90)
          .cutThruAll()
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, d2, d1*0.75))
          .transformed(rotate=(0, 90, 0))
          .slot2D(2*d2, d2, 90)
          .cutThruAll()
          #.extrude(10)
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, -d1/2, 0))
          .box(3*d1, d1/2, bracket_th , centered=(True, True, False))
          # round edges
          .edges("|Z or >Z").fillet(1)
          # mounting holes
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, -d1/2, 0))
          .rarray(2*d1, 1, 2, 1)
          .circle(4.5/2).cutThruAll()
)

show_object(result)

