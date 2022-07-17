import cadquery as cq
result = cq.Workplane("XY" ).box(5, 4.5, 3).faces(">Z").box(2.9, 1.9, 2.5, centered=(True, True, False)).edges("|Z").fillet(0.125).faces("<Z").rect(3.2, 2.1).cutBlind(2.5)
#