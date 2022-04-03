import cadquery as cq
import math

tube_r = 10 # tube radius
wth = 2 # tube wall thickness
shr = 2.7 # screw hole radius
shw = 7.5 # screw hole extra width

block_h = 20
upper_block_h = 3
oh = 3 # overhang of upper block
block_w = 85

pts = [(-5, 0), (-5, 5), (30, 5), (50, 25), (50, 55), (block_w, 55), (block_w, 25)]

pts2 = [(-5, 0), (-5, 5+oh), (30, 5+oh), (50-oh, 25), (50-oh, 55), (block_w, 55), (block_w, 25)]

s_pts =  [(block_w, 25), (30, 0)]

t_pts = [(0, -1), (-1, 0)]
 
block = (cq.Workplane("XY")
         .polyline(pts)
         .spline(s_pts, tangents=t_pts)
         .close()
         .extrude(block_h)
        )

upper_block = (cq.Sketch()
         .segment((-5.,0), (-5, 5+oh))
         .segment((30, 5+oh))
         .segment((50-oh, 25))
         .segment((50-oh, 55))
         .segment((block_w, 55))
         .segment((block_w, 25))
         .segment((50, 0))
         .close().assemble()
         #.extrude(upper_block_h)
        )

arcf = shr*math.cos(math.radians(45))

result = (
    block.faces(">Z")
    .transformed(offset=(67.5, 30, 0))
    .circle(tube_r+wth+0.5).cutThruAll()
    .faces("<Y").workplane(centerOption='CenterOfBoundBox')
    .transformed(offset=(-12, 0, 0))
    .threePointArc((shr-arcf, arcf), (shr, shr))
    .hLine(shw)
    .threePointArc((shr+shw+arcf, arcf), (shr+shw+shr, 0))
    .mirrorX()
    .cutThruAll()
    .faces(">Z").workplane()
    .transformed(offset=(0, 0, 0))
    .placeSketch(upper_block).extrude(upper_block_h)
)

show_object(result)
#show_object(upper_block)
