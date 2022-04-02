import cadquery as cq

path1 = cq.Workplane("XZ" ).vLine(50).tangentArcPoint([20, 25])

tube1 = cq.Workplane("XY").circle(10).sweep(path1).faces(">Z or <Z").shell(2)

path2 = cq.Workplane("XZ" ).vLine(50).tangentArcPoint([20, 25]).polarLine(20, 10)

#tube2 = cq.Workplane("XY").circle(10).sweep(path2).faces(">Z or <Z").shell(2)

#path2 = cq.Workplane("XZ" ).polarLine(20, 10)

#tube2 = cq.Workplane("YZ").circle(10).sweep(path2).faces(">Z or <Z").shell(2)

#path3 = path1.polarLine(20, 10)

#tube3 = tube1.faces("+Z").workplane().circle(10).sweep(path3)#.faces(">X or <X").shell(2)
