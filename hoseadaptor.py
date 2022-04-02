# 1

"""
Create a vacuum adaptor from 50mm to 30mm by:
1 - Draw the 2D shape on the XZ plane
2 - Revolve the shape around the Z axis
3 - Create a shell from the solid except for the top or bottom

The "show_object" code tells the cq-editor to show the object
"""
import cadquery as cq

MM = 1
adaptor = (cq.Workplane("XZ")
    .hLineTo(50*MM/2)
    .spline(listOfXYTuple = [(50*MM/2,0), (30*MM/2,50*MM)], tangents = [(0,1),(0,1)])
    .hLineTo(0)
    .close()
    .revolve()
    .faces(">Z or <Z")
    .shell(1*MM)
)

# 2

R1 = 30/2
R2 = 50/2
H = 30
TH = 1

res = (
    cq.Workplane()
    .circle(R1)
    .workplane(offset=H)
    .circle(R1)
    .workplane(offset=H)
    .circle(R2)
    .workplane(offset=H)
    .circle(R2)
    .loft(ruled=True)

    .faces(">Z or <Z")
    .shell(-TH)
)
