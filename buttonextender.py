import cadquery as cq
result = cq.Workplane("XY" ).box(5, 4.5, 8).faces(">Z").box(2.9, 1.9, 2.5, centered=(True, True, False)).edges("|Z").fillet(0.125).faces("<Z").rect(3.3, 2.3).cutBlind(4)
#