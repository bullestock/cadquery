import cadquery as cq

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

brim = cq.Workplane("XY").rect(brimWidth, brimDepth)\
.rect(headHoleWidth, headHoleDepth)\
.extrude(wallThickness)
# Fillet the vertical edges of the inside of the head hole
brim = brim.edges("|Z and (>>Y[-2] or <<Y[-2])").fillet(1)
# Fillet the vertical edges of the brim
brim = brim.edges("|Z and (>Y or <Y)").fillet(4)
# Create the hollowed out portion of the hat
hallowCap = cq.Workplane("XY")\
.rect(topHatWidth, topHatDepth)\
.rect(headHoleWidth, headHoleDepth)\
.extrude(hatHeight-topHatThickness)
# Fillet the inside vertical edges of the head hole
hallowCap = hallowCap.edges("|Z and (>>Y[-2] or <<Y[-2])").fillet(1)
# Fillet the outside vertical edges of the head hole
hallowCap = hallowCap.edges("|Z and (>Y or <Y)").fillet(2)
# Create the solid top portion of the hat
solidCap = cq.Workplane("XY")\
.rect(topHatWidth, topHatDepth)\
.extrude(topHatThickness)
solidCap.faces(">Z").workplane(centerOption="CenterOfMass").tag(">Z")
solidCap.faces(">X").workplane(centerOption="CenterOfMass").tag(">X")
solidCap.faces(">Y").workplane(centerOption="CenterOfMass").tag(">Y")
# Hallow out a portion of the solid cap
solidCap = solidCap.workplaneFromTagged(">Z")\
.hole(hatTopperDiameter)
# Fillet the outside vertical edges of the solid cap
solidCap = solidCap.edges("|Z and (>Y or <Y)").fillet(2)
# Create the x axis detent
solidCap = solidCap.workplaneFromTagged(">X")\
.move(0, topHatThickness/2)\
.hole(groveDepthDiameter)
# create the y axis detent
solidCap = solidCap.workplaneFromTagged(">Y")\
.move(0, topHatThickness/2)\
.hole(groveDepthDiameter)

hat = (
cq.Assembly(brim)

.add(hallowCap, loc=cq.Location(cq.Vector(0, 0, wallThickness)))
.add(solidCap, loc=cq.Location(cq.Vector(0, 0, wallThickness+(hatHeight-topHatThickness))))
)

show_object(hat)
