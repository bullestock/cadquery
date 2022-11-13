import cadquery as cq
import math
from cq_server.ui import ui, show_object

top_dia = 19.5
bot_dia = 18.5
h = 20
spout_id = 5
spout_od = 7
spout_h = 15
spout_offset = 4

seal_frac = 0.25
seal_dia = top_dia - (top_dia - bot_dia)*seal_frac + 0.5

# create path
path = (cq.Workplane("XY" )
        .circle(seal_dia/2)
        )

seal_d = 2.5
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
cq.exporters.export(res, 'dishstopper.stl')
