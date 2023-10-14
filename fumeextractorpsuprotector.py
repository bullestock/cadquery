import cadquery as cq

th = 1.5

res = (cq.Workplane("XY")
       .rect(31.5 + 2*th, 23.5 + 2*th)
       .extrude(25)
       .faces(">Z or <Z")
       .shell(-th)
       .edges("|Z")
       .fillet(2.5)
      )

show_object(res)
