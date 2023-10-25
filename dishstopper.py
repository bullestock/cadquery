import cadquery as cq
import math

top_dia = 18.5
bot_dia = 17
flange_dia = 20
flange_h = 3
h = 22
spout_id = 5
spout_od = 7
spout_h = 15
spout_offset = 4

seal_frac = 0.5
seal_dia = top_dia - (top_dia - bot_dia)*seal_frac - 1.0
log(seal_dia)

# create path
path = (cq.Workplane("XY" )
        .circle(seal_dia/2)
        )

seal_d = 3.5
seal_groove = (cq.Workplane("XZ")
               .transformed(offset=(seal_dia/2, (1-seal_frac)*h, 0))
               .circle(seal_d/2).sweep(path)
              )

res = (cq.Workplane("XY")
       .tag("bot")
       .circle(bot_dia/2)
       .workplane(offset=h)
       .circle(top_dia/2)
       .loft(combine=True)
       .faces(">Z")
       .circle(flange_dia/2)
       .extrude(flange_h)
       .edges(">Z").fillet(1)
       .workplaneFromTagged("bot")
       .transformed(offset=(spout_offset, 0, 0))
       .circle(spout_od/2)
       .extrude(h + spout_h)
       .workplaneFromTagged("bot")
       .transformed(offset=(spout_offset, 0, 0))
       .circle(spout_id/2)
       .cutThruAll() 
       .edges(">Z").fillet(0.49)
)

res = res - seal_groove

show_object(res)
