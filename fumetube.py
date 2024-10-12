import cadquery as cq
import math

wth = 2 # tube wall thickness
tube_r = 63.5/2 - 2*wth # tube inner radius
foot_r = 67/2
foot_h = 3.5
r1 = 100 # radius of bend
a1 = 90 # angle of bend in degrees

# Bend points
ap1 = (r1 - math.cos(math.radians(a1/2))*r1, math.sin(math.radians(a1/2))*r1)
ap2 = (r1 - math.cos(math.radians(a1))*r1, math.sin(math.radians(a1))*r1)

# create path
path = cq.Workplane("XZ" ).threePointArc(ap1, ap2).hLine(10)

# create tube by sweeping along path
tube = cq.Workplane("XY").circle(tube_r).sweep(path).faces(">X or <Z7ujn").shell(wth)

tube = (tube
        .faces("<Z")
        .tag("b")
        .circle(foot_r)
        .extrude(foot_h)
        .workplaneFromTagged("b")
        .circle(tube_r)
        .cutBlind(foot_h)
        )

show_object(tube)

