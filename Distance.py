import sys
from helpers import point_dist


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

    def safeAddPoints(self, point1, point2):
        dist_prime = point_dist(point1, point2)
        if dist_prime < self.distance:
            self.clearAndAddPoints(point1, point2)
            self.setDistance(dist_prime)
        elif dist_prime == self.distance:
            self.addPoints(point1, point2)


    def combine(self, distObj):
        if self.distance > distObj.getDistance():
            self.distance = distObj.getDistance()
            self.points = distObj.getPoints()
        elif  self.distance == distObj.getDistance():
            self.points = self.points + [i for i in distObj.getPoints() if i not in self.points]
        return self

    def prettyPrint(self):
        print("distance:")
        print(self.distance)
        print("points")
        print(self.points)
