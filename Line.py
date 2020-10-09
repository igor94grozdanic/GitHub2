import math
from Point import Point

class  Line(Point):

    def __init__(self, p1=Point(y=7500000, x=4000000), p2=Point(y=7500000, x=4500000)):
        Point.__init__(self)
        self.__p1 = p1
        self.__p2 = p2

    def getLength(self):
        return self.__p1.distance(self.__p2)

    def wktGeom(self):
        return 'LINE=(({0} {1}, {2} {3}))'.format(str(self.__p1.getYCoord()), str(self.__p1.getXCoord()),
                                                  str(self.__p2.getYCoord()), str(self.__p2.getXCoord()))
