import cadquery as cq
import math

tube_r = 10 # tube radius
d1 = 50 # height of vertical tube
r1 = 20 # radius of first bend
a1 = 80 # angle of first bend in degrees
d2 = 20 # length of horizontal tube
wth = 2 # tube wall thickness
r2 = 10 # radius of second bend
a2 = 80 # angle of second bend in degrees

# Bend points
ap1 = (r1 - math.cos(math.radians(a1/2))*r1, d1 + math.sin(math.radians(a1/2))*r1)
ap2 = (r1 - math.cos(math.radians(a1))*r1, d1 + math.sin(math.radians(a1))*r1)

# position of end of horizontal tube
bx =  r1 - math.cos(math.radians(a1))*r1 + math.cos(math.radians(90-a1))*d2
by = d1 + math.sin(math.radians(a1))*r1 + math.sin(math.radians(90-a1))*d2

# position of top of 90 degree bend from (bx, by)
tbx =  bx - math.cos(math.radians(a2))*r2
tby =  by + math.sin(math.radians(a2))*r2

#helper = cq.Workplane("XZ" ).hLine(tbx).vLine(tby).consolidateWires()

# position of top of final bend
fbtx = tbx + r2
fbty = tby
#fbthelper = cq.Workplane("XZ" ).hLine(fbtx).vLine(tby).consolidateWires()

# position of middle of final bend
fbmx = tbx + math.cos(math.radians(a2/2))*r2
fbmy = tby - math.sin(math.radians(a2/2))*r2
#fbmhelper = cq.Workplane("XZ" ).hLine(fbmx).vLine(fbmy).consolidateWires()

ap3 = (fbmx, fbmy)
ap4 = (fbtx, fbty)

#helper2 = cq.Workplane("XZ" ).hLine(ap3[0]).vLine(ap3[1]).consolidateWires()

#helper3 = cq.Workplane("XZ" ).hLine(ap4[0]).vLine(ap4[1]).consolidateWires()

path = cq.Workplane("XZ" ).vLine(d1).threePointArc(ap1, ap2).polarLine(d2, 90 - a1)#.threePointArc(ap3, ap4).consolidateWires()

tube = cq.Workplane("XY").circle(tube_r).sweep(path).faces(">Z or <Z").shell(wth)

show_object(tube)

cq.exporters.export(tube,'bungardtube.stl')
