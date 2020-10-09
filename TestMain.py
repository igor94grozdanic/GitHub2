import math
from Point import Point

from Line import Line

p1 = Point(7500000, 4500000)
p2 = Point(7500001, 4500001)
p3 = Point(7499999, 4500001)

print(p1.createLine(math.pi/2, 100))

l = Line(Point(7500000, 4500000), Point(7500001, 4500001))
print(l.getLength())
print(l.wktGeom())