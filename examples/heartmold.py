# 1

wire = (cq.Workplane("XY")

         .lineTo(2, 2)
         .threePointArc((4, 1), (3.5, 0))
         .mirrorX())

wire2 = wire.offset2D(-0.1).translate((0, 0, 0.1))

heart = wire.extrude(1.5)

heart = heart.wires("<Z").toPending().offset2D(-0.1).cutBlind(1.4).edges(">Z").fillet(0.5)

show_object(heart)

# 2

def heart():
    wire = (cq.Workplane("XY")
        .lineTo(2, 2)
        .threePointArc((4, 1), (3.5, 0))
        .mirrorX()
    )
    return (
        wire
        .extrude(1.5)
        .faces("<Z").shell(0.3, kind='intersection')
        .edges(">Z").fillet(0.1)
    )
show_object(heart())


# 3

def scale(workplane, x, y=None, z=None):
    """Scale workplane.
    
    From mbway: https://github.com/CadQuery/cadquery/issues/638
    """
    y = y if y is not None else x
    z = z if z is not None else x
    t = cq.Matrix([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]
    ])
    
    return workplane.newObject([
        o.transformGeometry(t) if isinstance(o, cq.Shape) else o
        for o in workplane.objects
    ])

def heart(scale=1):

    wire = cq.Workplane("XY") \
        .lineTo(scale*2, scale*2) \
        .threePointArc((scale*4, scale*1), (scale*3.5, 0)) \
        .mirrorX()
    
    return wire \
        .extrude(scale*1.5) \
        .edges(">Z") \
        .fillet(scale*1.2)

result = heart().cut(scale(heart(), 0.9).translate([0.2, 0, 0]))

# 4

outer = (
    cq.Workplane("XY")
    .lineTo(2, 2)
    .threePointArc((4, 1), (3.5, 0))
    .mirrorX()
    .extrude(-1.5)
    .edges("<Z")
    .fillet(1.2)
)
inner = (
    cq.Workplane("XY")
    .lineTo(2, 2)
    .threePointArc((4, 1), (3.5, 0))
    .mirrorX()
    .offset2D(-0.1, kind="intersection")
    .extrude(-1.4)
    .edges("<Z")
    .fillet(1.1)
)

heart = outer - inner
show_object(heart, name="heart")
