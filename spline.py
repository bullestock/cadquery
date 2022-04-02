# 1: Not parallel ends

points = [(0, 100), (0, 70), (10, 50), (0, 0)]

spline_path = cq.Workplane("YZ").spline(points)

solid = cq.Workplane("XY").circle(10).sweep(spline_path).faces(">Z or <Z").shell(2)

