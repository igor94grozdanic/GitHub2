import math

from Point import Point

p1 = Point(7500000 ,4500000)
p2 = Point(7500001 ,4500001)

print (p1.getCoord())
print (p2.getCoord())
dir = (p1.azimuth(p2)*180)/math.pi
dist = p1.distance(p2)

print ('Direkcioni ugao izmedju tacaka je {} stepeni!'.format(str(dir)))

print ('Duzina izmedju ovih tacaka je {} m!'.format(str(dist)))