import math

class Point:
    def __init__(self,y=7500000,x=4000000):
        self.__y=y
        self.__x=x

    def getCoord(self):
        return self.__y, self.__x

    def azimuth(self, to):
        dy = to.getCoord()[0] - self.getCoord()[0]
        dx = to.getCoord()[1] - self.getCoord()[1]
        ni = 0
        if dy == 0:
            if dx > 0:
                ni = 0
                return ni
            elif dx < 0:
                ni = math.radians(180)
                return ni
        elif dx == 0:
            if dy > 0:
                ni = math.radians(90)
                return ni
            elif dy < 0:
                ni = math.radians(270)
                return ni
        elif (dy > 0 and dx > 0):
            # print("1. kv:")
            ni = math.atan(dy / dx)
            return ni
        elif (dy > 0 and dx < 0):
            # print("2. kv:")
            ni = math.atan(abs(dx / dy)) + math.radians(90)
            return ni
        elif (dy < 0 and dx < 0):
            # print("3. kv:")
            ni = math.atan(dy / dx) + math.radians(180)
            return ni
        elif (dy < 0 and dx > 0):
            # print("4. kv:")
            ni = math.atan(abs(dx / dy)) + math.radians(270)
            return ni

    def distance(self,to):
        dy = to.getCoord()[0] - self.getCoord()[0]
        dx = to.getCoord()[1] - self.getCoord()[1]
        d = math.sqrt(math.pow(dy,2)+math.pow(dx,2))
        return d

