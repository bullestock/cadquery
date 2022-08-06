import cadquery as cq
from vypercamdefs import *

# Base

res = (cq.Workplane("XY")
       .tag("base")
       .circle(inner_d/2-0.2)
       .extrude(20)
       .workplaneFromTagged("base")
       .circle(outer_d/2)
       .extrude(10)
      )

show_object(res)

