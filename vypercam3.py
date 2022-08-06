import cadquery as cq
from vypercamdefs import *

# Base

res = (cq.Workplane("XY")
       .circle(middle_d/2-0.5)
       .extrude(4)
       .circle(inner_d/2-0.05)
       .cutThruAll()
      )

show_object(res)

