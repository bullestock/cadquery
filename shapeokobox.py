import cadquery as cq

width = 27
length = 70
height = 14

# shell thickness
th = 2.5
# shell fillet radius
fillet_r = 2

# make shell
result = (cq.Workplane("XY")
          .box(width, length, height/2)
          .faces(">Z")
          .shell(-th)
          # round edges
          .edges("<Z or |Z").fillet(fillet_r)
          )

show_object(result)
