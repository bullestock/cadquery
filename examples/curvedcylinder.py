# 1: Not parallel ends

points = [(0, 100), (20, 50), (0, 0)]

spline_path = cq.Workplane("YZ").spline(points)

solid = cq.Workplane("XY").circle(10).sweep(spline_path)

# 2: Parallel ends

h = 100
d = 20
points = [(0, h), (d, h/2), (0, 0)]


spline_path = cq.Workplane("YZ").spline(points)


solid = ( cq.Workplane("XY")
    .circle(10)
    .workplane(offset=h)
    .circle(10)
    .sweep(spline_path,multisection=True)
)
