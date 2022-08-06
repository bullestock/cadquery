import cadquery as cq

w = 25
gs = 25.4*1.5 # grid spacing
sd = 4 # depth of screw hole
th = 19 # thickness

def make_hole(o, x, y):
    return (o
            .workplaneFromTagged("bot")
            .transformed(offset=(w/2 + x*gs, w/2 + y*gs, 0))
            .tag("ref")
            .circle(6.2/2)
            .cutThruAll()
            .workplaneFromTagged("ref")
            .transformed(offset=(0, 0, th-sd))
            .circle(14/2)
            .cutBlind(sd)
            )

res = (cq.Workplane("XY")
       .tag("bot")
       .box(100, w, th, centered=False)
       .workplaneFromTagged("bot")
       .box(w, 100, th, centered=False)
       .edges(">Z or |Z")
       .fillet(2)
      )

res = make_hole(res, 0, 0)
res = make_hole(res, 0, 1)
res = make_hole(res, 0, 2)
res = make_hole(res, 1, 0)
res = make_hole(res, 2, 0)

res = (res
       .workplaneFromTagged("bot")
       .transformed(offset=(w, w, 0))
       .circle(3)
       .cutThruAll())
show_object(res)
