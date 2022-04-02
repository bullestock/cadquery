import cadquery as cq
import math

tube_r = 10 # tube radius
d1 = 50 # height of vertical tube
r1 = 20 # radius of bend
a1 = 80 # angle of bend in degrees
d2 = 20 # length of horizontal tube
wth = 2 # tube wall thickness

# Bend points
ap1 = (r1 - math.cos(math.radians(a1/2))*r1, d1 + math.sin(math.radians(a1/2))*r1)
ap2 = (r1 - math.cos(math.radians(a1))*r1, d1 + math.sin(math.radians(a1))*r1)

path = cq.Workplane("XZ" ).vLine(d1).threePointArc(ap1, ap2).polarLine(d2, 90 - a1).consolidateWires()

tube = cq.Workplane("XY").circle(tube_r).sweep(path).faces(">Z or <Z").shell(wth)

show_object(tube)
