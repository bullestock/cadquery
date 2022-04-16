import cadquery as cq

width = 100
d1 = 75
d2 = 50
depth = d1
bracket_th = 6
bracket_h = 50


result = (cq.Workplane("XZ")
          .vLine(bracket_th)
          .threePointArc((-d2/2, bracket_th+d2/2), (0, d2+bracket_th))
          .vLine(bracket_th)
          .threePointArc((-d2/2-bracket_th, bracket_th+d2/2), (0, 0))
          .close()
          .extrude(width)
          .faces("<Z").workplane(centerOption="CenterOfMass", 
                              invert=True).tag("bottom")
          .transformed(offset=(0, 0, bracket_h/2))
          .box(width, bracket_th, bracket_h)
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, -d1-bracket_th, 0))
          .slot2D(2*d1, d1, 90)
          .cutThruAll()
          .edges("|Z or >Z or >Y").fillet(1)

          )

show_object(result)

