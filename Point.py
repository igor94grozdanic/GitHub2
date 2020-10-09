import math

class Point:
    def __init__(self, p='point_id',y=7500000,x=4000000):
        self.p=p
        self.y=y
        self.x=x

    def getCoord(self):
        return self._y, self._x

    def azimuth(od, ka):
        dy = ka[0] - od[0]
        dx = ka[1] - od[1]
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