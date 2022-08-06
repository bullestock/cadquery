import cadquery as cq
from buttonboxdefs import *
import standoffs

height = 17

# ESP
holes_dx = 0.85 * 25.4

# esp standoff dimensions
standoff_h = 5
standoff_d = 7

esp_x_offset = 0
esp_y_offset = 17

usb_w = 11.5
usb_h = 6
usb_x_offset = 7.5
usb_z_offset = 11

standoff = standoffs.round_standoff(standoff_d, standoff_h)

screwpost_d = 8
screwpost_inset = 10.1
screwpost = standoffs.square_screwpost_body(screwpost_d, height-th, 2)

centerXY = (True, True, False)

# make shell
shell = (cq.Workplane("XY")
         .box(width, length, height, centered=centerXY)
         .faces(">Z")
         .shell(-th)
         # round edges
          .edges("<Z or |Z").fillet(fillet_r)
         )
shell.faces("<Z").workplane(centerOption="CenterOfMass", 
                            invert=True).tag("bottom")

# distribute standoffs
round_standoffs = (shell
             .workplaneFromTagged("bottom")
             # place standoffs on bottom
             .transformed(offset=(esp_x_offset, esp_y_offset, th+standoff_h/2))
             .rect(holes_dx, 0, forConstruction=True)
             .vertices()
             .eachpoint(lambda loc: standoff.val().moved(loc), True)
             )
rect_standoff = (shell
                 .workplaneFromTagged("bottom")
                 # place standoff on bottom
                 .transformed(offset=(esp_x_offset, esp_y_offset - 36, th))
                 .slot2D(17, 4, 0)
                 .extrude(standoff_h)
                )

# distribute screwposts and holes
screwposts = (shell
              .workplaneFromTagged("bottom")
              .transformed(offset=(0, 0, (th+height)/2))
              .rect(width - 1.2*screwpost_inset, length - 1.2*screwpost_inset, forConstruction=True)
              .vertices()
              .eachpoint(lambda loc: screwpost.val().moved(loc), True)
              )

# combine
result = shell.union(round_standoffs).union(rect_standoff).union(screwposts)

# screw holes
result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, (th+height)/2))
          .rect(width - 1.2*screwpost_inset, length - 1.2*screwpost_inset, forConstruction=True)
          .vertices()
          .circle(3.2/2)
          .cutThruAll()
          )
result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, 0))
          .rect(width - 1.2*screwpost_inset, length - 1.2*screwpost_inset, forConstruction=True)
          .vertices()
          .circle(screw_head_r)
          .cutBlind(screw_head_h)
          )

result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(usb_x_offset, -(length/2 - 10), usb_z_offset), rotate=(90, 0, 0))
          .slot2D(usb_w, usb_h, 0)
          .cutBlind(20)
          )
show_object(result)
