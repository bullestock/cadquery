import cadquery as cq

wallThickness = 1.3
hatHeight = 9.0
topHatThickness = 4.0
brimWidth = 31.7
brimDepth = 16.45
hatTopperDiameter = 4.9
headHoleWidth = 14.0
headHoleDepth = 7.8
topHatWidth = 16.5
topHatDepth = 10.2
groveDepthDiameter = 1.0

def makeRectFillet(length: float, width: float, radius:float=0.0, center:bool=True) -> cq.Wire:
    """
    Create a cq.Wire in the shape of a square with optionally rounded corners
    """
    # define the location of the center of the shape
    centerShift = cq.Vector(length/2,width/2,0) if not center else cq.Vector(0,0,0)
    hlr = length/2-radius
    hwr = width/2-radius
    if hlr<0 or hwr<0:
        raise ValueError("Fillet radius {} is too large for given rectangle dimension ({},{})".format(radius,length,width))
    r = cq.Wire.makePolygon([cq.Vector(hlr,hwr,0),cq.Vector(-hlr,hwr,0),cq.Vector(-hlr,-hwr,0),cq.Vector(hlr,-hwr,0),cq.Vector(hlr,hwr,0)])
    r = cq.Wire.assembleEdges(r.offset2D(radius)).translate(centerShift)
    return r
def _rectFillet(self, length: float, width: float, radius=0.0, center=True) -> cq.Workplane:
    """
    Create a cq.Workplane in the shape of a square with optionally rounded corners
    """
    r = makeRectFillet(length,width,radius,center)
    return self.eachpoint(lambda loc: r.moved(loc), True)
cq.Workplane.rectFillet = _rectFillet       # Add this custom method to the Workplane class

hat = (cq.Workplane("XY")
       .rectFillet(brimWidth,brimDepth,4)              # Define the brim as a ..
       .rectFillet(headHoleWidth,headHoleDepth,1)      # .. filleted rectangle with a ..
       .extrude(wallThickness)                         # .. filleted rectangular hole of wallThickness
       .faces(">Z").workplane()                        # On the top of the brim ..
       .rectFillet(topHatWidth,topHatDepth,2)          # .. create the walls of the hat ..
       .rectFillet(headHoleWidth,headHoleDepth,1)      # .. as the difference between two filleted ..
       .extrude(hatHeight-topHatThickness)             # .. rectangles extruded to the cap
       .faces(">Z").workplane()                        # On the top of the hat walls ..
       .rectFillet(topHatWidth,topHatDepth,2)          # .. create a cap with a ..
       .circle(hatTopperDiameter/2)                    # .. circular hole in it of ..
       .extrude(topHatThickness)                       # .. thickness topHatThickness
       # Create two perpendicular semi-circular slots across the top of the hat
       .cut(cq.Solid.makeCylinder(groveDepthDiameter/2,topHatWidth,pnt=cq.Vector(-topHatWidth/2,0,wallThickness+hatHeight),dir=cq.Vector(1,0,0)))
       .cut(cq.Solid.makeCylinder(groveDepthDiameter/2,topHatDepth,pnt=cq.Vector(0,-topHatDepth/2,wallThickness+hatHeight),dir=cq.Vector(0,1,0)))
       )

show_object(hat, name="hat")
