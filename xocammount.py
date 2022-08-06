import cadquery as cq

w = 7.5
h = 50

res = (cq.Workplane("XY")
       .box(13.3, w, h, centered=(True, True, False))
       .edges(">Z and |X")
       .fillet(w/2-0.01)
       .workplane()
       .transformed(offset=(0, 0, (h - w)/2), rotate=(90, 90, 0))
       .circle(4/2)
       .cutThruAll()
      )

show_object(res)
