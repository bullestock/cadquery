import cadquery as cq

res = (cq.Workplane("XY")
       .tag("bot")
       .box(91, 91, 31, centered=(True, True, False))
       .edges(">Z or |Z")
       .fillet(3)
       .workplaneFromTagged("bot")
       # cutout for base
       .rect(86, 86)
       .cutBlind(12)
       # cutout for keys
       .workplaneFromTagged("bot")
       .transformed(offset=(0, -1, 0))
       .rect(77, 77)
       .cutThruAll()
       # USB plug hole
       .workplaneFromTagged("bot")
       .transformed(offset=(0, 0, 15.5), rotate=(90, 0, 0))
       .slot2D(13, 8)
       .cutBlind(50)
       # printing help
       .transformed(offset=(0, -3.5, 15))
       .rect(13, 8)
       .cutBlind(28)
      )

show_object(res)
