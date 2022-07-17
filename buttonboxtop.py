import cadquery as cq
import math
from buttonboxdefs import *

height = 20

centerXY = (True, True, False)

# make shell
result = (cq.Workplane("XY")
          .box(width, length, height)
          .faces("<Z")
          .shell(-th)
          # round edges
         .edges("|Z").fillet(fillet_r)
          .faces(">Z")
          .edges().fillet(fillet_r)
          )

result.faces("<Z").workplane(centerOption="CenterOfMass", 
                             invert=True).tag("bottom")

result.faces("<Z").workplane(centerOption="CenterOfMass").tag("top")

screwpost_d = 10.1 # must be > 2*fillet_r

def make_screwpost(o, xs, ys):
    ovec = (xs*(width - 1.2*screwpost_d)/2, ys*(length - 1.2*screwpost_d)/2, 0)
    return (o
            .workplaneFromTagged("bottom")
            .transformed(offset=ovec)
            .rect(screwpost_d, screwpost_d)
            .extrude(until='next')
            .edges("|Z")
            .fillet(2)
            .workplaneFromTagged("bottom")
            .transformed(offset=ovec)
            .circle(insert_sr+.25)
            .cutBlind(height-th)
            .workplaneFromTagged("bottom")
            .transformed(offset=ovec)
            .circle(insert_r)
            .cutBlind(insert_l)
            )

result = make_screwpost(result, -1, -1)
result = make_screwpost(result, -1,  1)
result = make_screwpost(result,  1, -1)
result = make_screwpost(result,  1,  1)

button_spacing = 30

# increase thickness where buttons are
button_nut_dia = 18
result = (result
          .workplaneFromTagged("top")
          .transformed(offset=(0, 0, -height+th))
          .slot2D(2*button_spacing+button_nut_dia, button_nut_dia, 90)
          .extrude(th)
          )

def make_button_hole(o, offset):
    ovec = (0, offset*button_spacing, 0)
    return (o
            .workplaneFromTagged("top")
            .transformed(offset=ovec)
            .circle(6.5)
            .cutThruAll()
            )

result = make_button_hole(result, -1)
result = make_button_hole(result, 0)
result = make_button_hole(result, 1)    

show_object(result)
