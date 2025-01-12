import cadquery as cq

d1 = 17.7
d2 = 16
d3 = 3
d4 = 22
d5 = 8
d6 = 18
d7 = 12

res = cq.Workplane("XY")

for i in range(0, 5):
    res = (res
           .workplane()
           .circle(d2/2)
           .workplane(d3)
           .circle(d1/2)
           .loft()
           .faces(">Z")
           )

# foot
res = (res
       .faces(">Z")
       .workplane()
       .circle(d4/2)
       .workplane(d5)
       .transformed(rotate=(10, 0, 0))
       .circle(d6/2)
       .loft()
       .faces(">Z")
    .fillet(1)       
       # inner hole
       .faces("<Z")
       .workplane()
       .circle(d7/2)
       .cutBlind(-d3*5)
       )

show_object(res)
