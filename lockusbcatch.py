import cadquery as cq

th = 3.5
w = 11
oh = 6
h = 45

res = (cq.Workplane("XY")
       .tag("bot")
       .box(oh+th, w, th, centered=False)
       .workplaneFromTagged("bot")
       .transformed(offset=(0, w/2, 0))
       .circle(8/2)
       .cutThruAll()
       .workplaneFromTagged("bot")
       .transformed(offset=(oh, 0, th))
       .box(th, w, h, centered=False)
       .edges("|Z")
       .fillet(0.5)
      )

res = (res
       .workplaneFromTagged("bot")
       .transformed(offset=(oh+th-0.2, 0, h*0.5), rotate=(90, 0, 0))
       .slot2D(25, 5, 90)
       .cutThruAll()
          )

show_object(res)
