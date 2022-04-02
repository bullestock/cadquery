result = cq.Workplane("XY").circle(spoolRadius).extrude(spoolWidth)\

.faces("<Z").workplane().polygon(6, hexRadius*2).extrude(hexWidth)\

.faces(">Z").workplane().polygon(22, spoolRadius*2-5).vertices().hole(indexDia)\

.faces(">Z").workplane().hole(shaftDia)\

.faces("|Z").chamfer(.3999)


