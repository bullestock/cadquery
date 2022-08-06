import cadquery as cq
from buttonboxdefs import *
import standoffs

# esp standoff dimensions
standoff_h = 5
standoff_d = 7

rect_standoff = (cq.Workplane("XY")
                 .slot2D(17, 4, 0)
                 .extrude(standoff_h)
                )
show_object(rect_standoff)
