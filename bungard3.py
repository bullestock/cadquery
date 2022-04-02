import cadquery as cq

tube_r = 10 # tube radius
block_h = 10

pts = [(0, 0), (0,5), (30, 5), (50, 25), (50, 55), (80, 55), (80, 25), (50, 0)]

block = (cq.Workplane("YZ")
         .polyline(pts)
         .close()
         .extrude(block_h, both=True)
        )

result = block

show_object(result)

