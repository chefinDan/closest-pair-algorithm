# Author: Daniel Green, greendan@oregonstate.edu
#
# Usage: put the helpers.py file in the same directory as this file.
# change string var "file" to be whichever file you want to run.
#

from helpers import point_dist


def brute_force(pointlist, distObj):
    point1 = pointlist[0]
    point2 = pointlist[1]
    min = point_dist(point1, point2)  # use the first set of points
    ln = len(pointlist)

    if (ln == 2):
        if min < distObj.getDistance():
            distObj.setDistance(min)
            distObj.clearAndAddPoints(point1, point2)
        elif min == distObj.getDistance():
            distObj.addPoints(point1, point2)
        return distObj
    else:
        for i in range(ln-1):
            for j in range(i + 1, ln):  # range of j gets smaller as traversal

                if i != 0 and j != 1:  # if the end of the list has not reached
                    dist = point_dist(pointlist[i], pointlist[j])
                    if dist < distObj.getDistance():  # Update min_dist and points
                        distObj.setDistance(dist)
                        distObj.clearAndAddPoints(pointlist[i], pointlist[j])
                        point1, point2 = pointlist[i], pointlist[j]
                    elif dist == distObj.getDistance():
                        distObj.addPoints(pointlist[i], pointlist[j])
        return distObj


def main():

    if __name__ == "__main__":
        main()
