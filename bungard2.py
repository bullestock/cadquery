import cadquery as cq

tube_r = 10 # tube radius
nozzle_h = 5
length = 20
wth = 2 # tube wall thickness
ring_h = 5

#rr = cq.Workplane("XY").rect(tube_r, 5).fillet(1)

ring = cq.Workplane("XY").circle(tube_r-0.2).extrude(ring_h).faces("<Z or > Z").shell(-wth)

outer = (cq.Workplane("XY").
    circle(tube_r + wth). # circular bottom
    workplane(offset=length).transformed(offset=(0, tube_r+wth, 0)).
    rect(tube_r, nozzle_h). # rectangular top
    loft(combine=True).     # combine
    edges(">Z").fillet(1)   # round edges
)

inner = (cq.Workplane("XY").
    circle(tube_r-wth). # circular bottom
    workplane(offset=length).transformed(offset=(0, tube_r+wth, 0)).
    rect(tube_r-wth, nozzle_h-wth). # rectangular top
    loft(combine=True)     # combine
)

result = ring.translate((0, 0, -ring_h)) + outer - inner
show_object(result)
#show_object(inner)
