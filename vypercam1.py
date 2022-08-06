import cadquery as cq
from vypercamdefs import *

# Base

res = (cq.Workplane("XY")
       .circle(outer_d/2)
       .extrude(10)
       .circle(inner_d/2)
       .cutThruAll()
       .circle(middle_d/2)
       .cutBlind(5)
      )

show_object(res)

