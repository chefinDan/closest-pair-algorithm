import sys


class Distance:
    def __init__(self):
        self.distance = sys.maxint
        self.points = []

    def getPoints(self):
        return self.points

    def getDistance(self):
        return self.distance

    def addPoints(self, point1, point2):
        self.points.append((point1, point2))

    def setDistance(self, distance):
        self.distance = distance

    def clearAndAddPoints(self, point1, point2):
        del self.points[:]
        self.points.append((point1, point2))
