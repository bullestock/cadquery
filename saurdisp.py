import cadquery as cq
import math

# shell thickness
th = 3
# shell fillet radius
fillet_r = 5

disp_hole_w = 71
disp_hole_h = 51
disp_w = 80
disp_h = 57
disp_h_cc_x = 85
disp_h_cc_y = 50.8

centerXY = (True, True, False)

bot_depth = 55
top_depth = 25
height = 70
width = 105

# make shell
result = (cq.Workplane("XZ")
          .hLine(bot_depth)
          .vLine(height)
          .hLine(-top_depth)
          .lineTo(0, 0)
          .close()
          .extrude(width)
          .faces("<Z")
          .shell(-th)
          # round back edges
          .edges("|Z").fillet(fillet_r)
          # round top
          .faces(">Z")
          .edges().fillet(fillet_r)
          # round front edges
          .edges('|(30, 0, 70)').fillet(fillet_r)
          )

# workplane aligned with front face
angle = math.degrees(math.atan(height/(bot_depth-top_depth)))
(result
 .faces("<Z")
 .workplane(centerOption="CenterOfMass", invert=True)
 .transformed(offset=(-13, 0, 32), rotate=(0, -angle, 0))
 .tag("front")
)

# for debugging
#result = result.workplaneFromTagged("front").box(50, 50, 10, centered=centerXY)

disp_y_offset = 3
# hole for display
result = (result
          .workplaneFromTagged("front")
          .transformed(offset=(disp_y_offset, 0, th))
          .rect(disp_hole_h, disp_hole_w)
          .cutBlind(-10)
          )
# recess for display
result = (result
          .workplaneFromTagged("front")
          .transformed(offset=(disp_y_offset-1.5, 0, -5))
          .rect(disp_h, disp_w)
          .cutBlind(th)
          )
# screwposts for display
def make_disp_screwpost(o, xs, ys):
    ovec1 = (disp_y_offset+xs*disp_h_cc_y/2, ys*disp_h_cc_x/2, -2)
    ovec2 = (disp_y_offset+xs*disp_h_cc_y/2, ys*disp_h_cc_x/2, -th)
    return (o
            .workplaneFromTagged("front")
            .transformed(offset=ovec1)
            .circle(3)
            .extrude(-3.5)
            .workplaneFromTagged("front")
            .transformed(offset=ovec2)
            .circle(1.25)
            .cutBlind(-10)
            )

result = make_disp_screwpost(result, -1, -1)
result = make_disp_screwpost(result, -1,  1)
result = make_disp_screwpost(result,  1, -1)
result = make_disp_screwpost(result,  1,  1)

# slots
def make_slot(xo):
    groove_offset = -1
    if xo > 0:
        groove_offset = 1
    return (cq.Workplane("XY")
            .transformed(offset=(bot_depth-7.5, -5/2 - xo*(width-5), 0))
            .box(8, 5, height-fillet_r, centered=centerXY)
            .transformed(offset=(0, groove_offset, height-fillet_r))
            .rect(3, 3)
            .cutBlind(-height)
            )

result = result + make_slot(0)
result = result + make_slot(1)

# back cutout
cutout_w = width - 2* fillet_r
cutout = (cq.Workplane("ZY")
          .transformed(offset=(0, -cutout_w-(width-cutout_w)/2, -bot_depth-5))
          .box(height - fillet_r, cutout_w, 10, centered=False)
          )

result = (result - cutout)

# mount
mount_h = 12
mount_w = width - 2*th
mount_d = bot_depth - 10
mount = (cq.Workplane("XY")
         .transformed(offset=(th, -width+(width-mount_w)/2, -(mount_h-th)))
         .box(mount_d, mount_w, mount_h, centered=False)
         .faces("<Z or >Z")
         .shell(-th)
         )

result = (result + mount)

show_object(result)
