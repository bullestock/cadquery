import cadquery as cq

# Create three tabs that will be extruded on a face of the box
tabs = cq.Sketch().rarray(30, 1, 3, 1).rect(25, 10)
box = (
    cq.Workplane("XY")
    # Base shape
    .box(50, 100, 15)
    # On the top
    .faces(">Z")
    .tag("top_of_box")
    .workplane()
    # Create a cylindrical feature
    .circle(5)
    .extrude(10)
    # On the front
    .faces("<Y")
    .workplane(origin=(0, 0))
    # Create a hole
    .circle(5)
    .extrude(-10, combine="cut")
    # On the side
    .faces(">X")
    .workplane(origin=(0, 0))
    # Create three tabs
    .placeSketch(tabs)
    .extrude(10)
    # Use the tag
    .faces(tag="top_of_box")
    .workplane()
    .center(-10, 0)
    .rect(10, 10)
    .extrude(5)
)

