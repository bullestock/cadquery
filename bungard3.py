import cadquery as cq

tube_r = 10 # tube radius
wth = 2 # tube wall thickness

block_h = 10
block_w = 85

pts = [(0, 0), (0,5), (30, 5), (50, 25), (50, 55), (block_w, 55), (block_w, 25)]
s_pts =  [(block_w, 25), (30, 0)]

t_pts = [(0, -1), (-1, 0)]
 
#         .spline(pts, tangents=t_pts)

block = (cq.Workplane("XY")
         .polyline(pts)
         .spline(s_pts, tangents=t_pts)
         .close()
         .extrude(block_h)
        )

result = (
    block.faces(">Z")
    .transformed(offset=(67.5, 30, 0))
    .circle(tube_r+wth).cutThruAll()
    .faces("<Y").workplane(centerOption='CenterOfBoundBox')
    .transformed(offset=(-5, 0, 0))
    .circle(2.7).cutThruAll()
)

show_object(result)

