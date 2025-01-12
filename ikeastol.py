import cadquery as cq

d1 = 18
d2 = 16
d3 = 3
d4 = 22
d5 = 8
d6 = 18
d7 = 12

res = (cq.Workplane("XY")
       .circle(d6/2)
       .workplane(d5)
       .circle(d4/2)
       .loft()
       .circle(d1/2)
       .workplane(d3)
       .circle(d2/2)
       .loft()
       .faces(">Z")
       .workplane()
       .circle(d1/2)
       .workplane(d3)
       .circle(d2/2)
       .loft()
       .faces(">Z")
       .workplane()
       .circle(d1/2)
       .workplane(d3)
       .circle(d2/2)
       .loft()
       .faces(">Z")
       .workplane()
       .circle(d1/2)
       .workplane(d3)
       .circle(d2/2)
       .loft()
       .faces(">Z")
       .workplane()
       .circle(d1/2)
       .workplane(d3)
       .circle(d2/2)
       .loft()
       .faces(">Z")
       .workplane()
       .circle(d1/2)
       .workplane(d3)
       .circle(d2/2)
       .loft()
       .faces(">Z")
       .workplane()
       .circle(d7/2)
       .cutBlind(-d3*5)
       )

show_object(res)
