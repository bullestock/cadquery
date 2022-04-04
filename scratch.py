import cadquery as cq
import math

shr = 2.7 # screw hole radius
shw = 5 # screw hole extra width
arcf = shr*1/math.sqrt(2)

res = (cq.Workplane("XY")
       .threePointArc((shr-arcf, arcf), (shr, shr))
       .hLine(shw)
       .threePointArc((shr+shw+arcf, arcf), (shr+shw+shr, 0))
       .consolidateWires()
      )
h = cq.Workplane("XY").hLine(shr-arcf).vLine(arcf).consolidateWires()
show_object(res)
show_object(h)