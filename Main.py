import math

from Point import Point

p1 = Point(7500000, 4500000)
p2 = Point(7500001, 4500001)
p3 = Point(7499999, 4500001)

print (p1.getCoord())
print (p2.getCoord())
dir = (p1.azimuth(p2)*180)/math.pi
dist = p1.distance(p2)

newborderAngle1 = (p1.newBorderAzimuth(p1.azimuth(p2))*180)/math.pi
newborderAngle3 = (p1.newBorderAzimuth(p1.azimuth(p3))*180)/math.pi

print ('Direkcioni ugao izmedju tacaka je {} stepeni!'.format(str(dir)))

print ('Duzina izmedju ovih tacaka je {} m!'.format(str(dist)))

print ('Direkcioni ugao nove granicne linije je {} stepeni!'.format(str(newborderAngle1)))

print ('Direkcioni ugao nove granicne linije je {} stepeni!'.format(str(newborderAngle3)))