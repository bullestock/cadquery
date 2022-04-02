import cadquery as cq

boxL = 30.0
boxW = 20.0
boxH = 10.0
boxT = 1.5
rout = 2.0
rin = 1.0
slotH = 2
doorW = 20
doorH = 5

plan = cq.Sketch().rect(boxL, boxW).vertices().fillet(rout)
cutout = (
    cq.Sketch()
    # Locate center of the slot
    .push([(0, boxT + slotH / 2)]).rect(boxL - 2 * boxT, slotH)
    # Locate center of the door
    .push([(0, boxT + doorH / 2)])
    # Combine the door with the slot
    .rect(doorW, doorH, mode="a")
    # Remove internal edges
    .clean()
)
box2 = (
    cq.Workplane("XY")
    .placeSketch(plan)
    .extrude(boxH)
    # Select the top as being open
    .faces(">Z")
    # Create a shell going inwards by boxT
    .shell(-boxT)
    # On the front of the box
    .faces("<Y")
    .workplane()
    # Place the cutout sketch and cut the hole
    .placeSketch(cutout)
    .cutThruAll()
)
