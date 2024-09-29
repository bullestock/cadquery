import cadquery as cq

w1 = 80
w2 = 71
h1 = 70
h2 = 52
r = 5
th = 4
foot_r = 2
foot_h = 5
hole_r = 2
hole_cc = 6

result = (cq.Workplane("XY")
          # lower left corner
          .moveTo(0, r)
          .radiusArc((r, 0), -r)
          .hLine(w2 - 2*r)
          # lower right corner
          .radiusArc((w2, r), -r)
          .lineTo(w2, h2)
          # middle corner
          .hLine(w1 - w2 - r)
          .radiusArc((w1, h2 + r), -r)
          .lineTo(w1, h1 + h2 - r)
          # upper right corner
          .radiusArc((w1 - r, h1 + h2), -r)
          .hLine(-(w1 - 2*r))
          # upper left corner
          .radiusArc((0, h1 + h2 - r), -r)
          .close()
          .extrude(th)
          .faces("Z")
          .workplane()
          .tag("top")
          # feet
          .transformed(offset=(w1/2, h1/2 + h2, 0))
          .rarray(w1 - 2*foot_r, h1 - 2*foot_r - r, 2, 2)
          .circle(foot_r)
          .extrude(foot_h)
          .workplaneFromTagged("top")
          .transformed(offset=(w2/2, r, 0))
          .rarray(w2 - 2*foot_r, 1, 2, 1)
          .circle(foot_r)
          .extrude(foot_h)
          # sieve holes
          .workplaneFromTagged("top")
          .transformed(offset=(w2/2 + 1, (h1 + h2)/2 + 3, 0))
          .rarray(hole_cc, hole_cc, int(w1/hole_cc) - 2, int((h1 + h2)/hole_cc) - 1)
          .circle(hole_r)
          .cutThruAll()
          .workplaneFromTagged("top")
          .transformed(offset=(w2 + 2, h1/2 + h2 + 1, 0))
          .rarray(1, hole_cc, 1, int(h1/hole_cc))
          .circle(hole_r)
          .cutThruAll()
)

show_object(result)

