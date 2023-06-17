import cadquery as cq

th = 3
iw = 15.5
ol = 125
ih = 2+2+5
oh = ih + 2*th
fillet_r = 7.49 

centerXY = (True, True, False)

# make shell
result = (cq.Workplane("XY")
         .box(iw + 2*th, ol, ih + 2*th, centered=centerXY)
         .shell(-th)
         # round edges
         .edges("<Z or >Z or |Z").fillet(fillet_r)
         )

result.faces("<Z").workplane(centerOption="CenterOfMass", 
                            invert=True).tag("bottom")

# wire hole
result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, oh/2), rotate=(90, 0, 0))
          .circle(3/2)
          .cutBlind(ol)
          )

# probe hole
result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, th+2), rotate=(90, 0, 0))
          .rect(5.75, 2.5)
          .cutBlind(-ol)
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 0, th+3), rotate=(90, 0, 0))
          .circle(1)
          .cutBlind(-ol)
          )

# pcb stops
result = (result
          .workplaneFromTagged("bottom")
          .transformed(offset=(0, 58-80.5, 1))
          .rarray(iw - 5, 1, 2, 1)
          .circle(1.5)
          .extrude(ih)
          )


cut_h = ih + 1

# top
p1 = result.workplaneFromTagged("bottom").workplane(cut_h).split(keepTop=True)

# bottom
p2 = result.workplaneFromTagged("bottom").workplane(cut_h).split(keepBottom=True)

# studs for keeping parts together
stud_d = 3
p1 = (p1
      .workplaneFromTagged("bottom")
      .workplane(ih-1)
      .rarray(iw - stud_d, (ol - 5*th - 2*stud_d)/2, 2, 3)
      .circle(stud_d/2)
      .extrude(5)
      .workplaneFromTagged("bottom")
      .workplane(ih-1)
      .rarray(1, ol - 2*th - stud_d, 1, 2)
      .circle(stud_d/2)
      .extrude(5)
     )

# LED holes
led_d = 2

def addtext(o, text, offset):
    return (o
      .workplaneFromTagged("bottom")
      .transformed(offset=(4, -ol/2 + offset, oh), rotate=(0, 0, 90))
      .text(text,
            7, 
            -1.5,
            cut=True,
            halign="center", 
            valign="bottom", 
            font="Sans",
            kind="bold"
       ) 
      )

p1 = (p1
      .workplaneFromTagged("bottom")
      .transformed(offset=(-3.15, -ol/2 + 58.3, 0))
      .circle(led_d/2)
      .cutThruAll()
      .workplaneFromTagged("bottom")
      .transformed(offset=(-3.15, -ol/2 + 65.3, 0))
      .circle(led_d/2)
      .cutThruAll()
      .workplaneFromTagged("bottom")
      .transformed(offset=(-3.15, -ol/2 + 72.3, 0))
      .circle(led_d/2)
      .cutThruAll()
     )

p1 = addtext(p1, "H", 57.6)
p1 = addtext(p1, "L", 64.8)
p1 = addtext(p1, "Z", 71.8)

#show_object(p1)
show_object(p2)
