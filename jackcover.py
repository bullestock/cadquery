import cadquery as cq
from vypercamdefs import *

# Base

res = (cq.Workplane("XY")
       .tag("o")
       .circle(9/2)
       .extrude(18)
       .faces("<Z")
       .circle(3.7/2)
       .cutBlind(15)
       .faces(">Z")
       .fillet(4)
       .faces(">Z")
       .workplane(-5)
       .rarray(1, 4, 1, 2)
       .box(5, 1, 1)
      )

show_object(res)

