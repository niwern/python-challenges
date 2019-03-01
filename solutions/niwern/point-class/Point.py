from math import atan, pi


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**.5

    def angle_to(self, point):
        x = (point.y - self.y)/(point.x - self.x)
        return atan(x)*180/pi
