import cadquery as cq
import math

tube_r = 10 # tube radius
wth = 2 # tube wall thickness
shr = 2.7 # screw hole radius
shw = 10 # screw hole extra width

# dimensions of M8 fixing nut
nut_r1 = 6.5
nut_r2 = 7.5
nut_th = 6.5

block_h = 20
upper_block_h = 3
oh = 3 # overhang of upper block
block_w = 90

# radius of round corner
arc_r = 35
# compute midpoint of arc
arc_x = block_w - (arc_r - arc_r*math.cos(math.radians(45)))
arc_y = arc_r - arc_r*math.sin(math.radians(45))

pts = [(-5, 0), (-5, 5), (30, 5), (50, 25), (50, 58), (block_w, 58), (block_w, arc_r)]

# lower block
block = (cq.Workplane("XY")
         .polyline(pts)
         .threePointArc((arc_x, arc_y), (block_w-arc_r, 0))
         .close()
         .extrude(block_h)
        )

# upper block
upper_block = (cq.Sketch()
               # annoyingly, polyline is not supported for sketch
               .segment((-5.,0), (-5, 5+oh))
               .segment((30+oh, 5+oh))
               .segment((50-2.5*oh, 25-2.5*oh))
               .segment((50-2.5*oh, 58))
               .segment((block_w, 58))
               .segment((block_w, arc_r))
               # arc, not threePointArc
               .arc((block_w, arc_r), (arc_x, arc_y), (block_w-arc_r, 0))
               .close()
               .assemble()
              )

# compute midpoint of arc for screw hole
arcf = shr*math.cos(math.radians(45))

result = (
    # place lower block
    block
    # construct elongated screw hole:
    .faces("<Y").workplane(centerOption='CenterOfBoundBox')
    .transformed(offset=(-25, 0, 0))
    # quarter arc
    .threePointArc((shr-arcf, arcf), (shr, shr))
    # straight line
    .hLine(shw)
    # quarter arc
    .threePointArc((shr+shw+arcf, arcf),
                   (shr+shw+shr, 0))
    # mirror
    .mirrorX()
    # make hole
    .cutThruAll()
    # put upper block on top and extrude it
    .faces(">Z").workplane(origin=(0, 0, 0))
    .transformed(offset=(0, 0, 0))
    .placeSketch(upper_block).extrude(upper_block_h)
    # make tube hole
    .faces(">Z")
    .transformed(offset=(67.5, 40, 0))
    .tag("tubehole")
    .circle(tube_r+wth+0.15).cutThruAll()
    # fixing screw hole
    .workplaneFromTagged("tubehole")
    .transformed(offset=(0, 0, -block_h/2), rotate=(0, -90, 0))
    .circle(4.5).cutBlind(-3*tube_r)
    # nut hole
    .workplaneFromTagged("tubehole")
    .transformed(offset=(tube_r+3.5*wth, 0, -block_h/2+nut_r1))
    .rect(nut_th, 2*nut_r2).cutBlind(-20)
    # cutout for Kress
    .workplaneFromTagged("tubehole")
    .transformed(offset=(-25, 0, 0))
    .circle(6)
    .cutThruAll()
)

show_object(result)

