wallThickness = 1.3
hatHeight = 9.0
topHatThickness = 4.0
pegHeight = 8.0
pegDiameter = 3.45
pegSubtraction = 0.02
brimWidth = 31.7
brimDepth = 16.45
hatTopperDiameter = 4.9
headHoleWidth = 14.0
headHoleDepth = 7.8
topHatWidth = 16.5
topHatDepth = 10.2
groveDepthDiameter = 1.0

hat2 = (
    cq.Workplane()
    .box(brimWidth, brimDepth, wallThickness, centered=(True, True, False))
    .tag("brim")
    .faces(">Z")
    .workplane()
    .box(topHatWidth, topHatDepth, hatHeight, centered=(True, True, False))
)

for sel in ["X", "Y"]:
    hat2 = (
        hat2
        .faces(">" + sel + "[1]")
        .edges(">Z")
        .workplane(centerOption="CenterOfMass")
        .hole(groveDepthDiameter)
    )

hat2 = (
    hat2
    .faces("<Z")
    .workplane(centerOption="ProjectedOrigin", origin=(0, 0, 0))
    .rect(headHoleWidth, headHoleDepth)
    .cutBlind(-(hatHeight - topHatThickness))
    .faces(">Z")
    .workplane()
    .hole(hatTopperDiameter)
    .edges("|Z", tag="brim")
    .fillet(4)
    .faces(">X[1] or >X[4]")
    .edges("|Z")
    .fillet(2)
    .faces(">X[2] or >X[3]")
    .edges("|Z")
    .fillet(1)
)

show_object(hat2, "hat2")
