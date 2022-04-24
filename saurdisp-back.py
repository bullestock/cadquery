import cadquery as cq
import math

# shell thickness
th = 3
# shell fillet radius
fillet_r = 5

centerXY = (True, True, False)

bot_depth = 55
top_depth = 25
height = 70
width = 105
back_w = width - 2* fillet_r - 0.05
back_h = height - fillet_r - 0.2
back_th = 9

def make_tab(xo):
    tab_x = 3-0.2
    tab_y = 3-0.5
    return (cq.Workplane("XY")
            .transformed(offset=(-back_th+tab_x/2, xo*back_w/2+xo*tab_y/2, back_h/2))
            .rect(tab_x, tab_y)
            .extrude(-back_h)
            )

back = (cq.Workplane("ZY")
        .transformed(offset=(0, 0, 0))
        .box(back_h, back_w, back_th, centered=centerXY)
        )

result = back + make_tab(1) + make_tab(-1)

show_object(result)
