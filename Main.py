from Point import Point

p1 = Point(7500000 ,4500000)
p2 = Point(7500001 ,4500001)

print (p1.getCoord())
print (p2.getCoord())
dir = (p1.azimuth(p2)*180)/math.pi

print ('Direkcioni ugao izmedju tacaka je {}!'.format(str(dir)))