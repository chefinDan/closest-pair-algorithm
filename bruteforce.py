# Author: Daniel Green, greendan@oregonstate.edu
#
# Usage: put the helpers.py file in the same directory as this file.
# change string var "file" to be whichever file you want to run.
#

from helpers import point_dist
import sys


def file_len_list(file_name):
    points = []
    with open(file_name) as f:
        for point_count, point in enumerate(f):
            points.append(point.strip())
    return point_count + 1, points


def brute_force(pointlist, distDict):
    point1 = pointlist[0]
    point2 = pointlist[1]
    min = point_dist(point1, point2)  # use the first set of points
    ln = len(pointlist)

    if (ln == 2):
        # d = point_dist(point1, point2)
        distDict[(point1, point2)] = {'Dist': min}
        return min, point1, point2
    else:
        for i in range(ln-1):
            for j in range(i + 1, ln):  # range of j gets smaller as traversal

                if i != 0 and j != 1:  # if the end of the list has not reached
                    dist = point_dist(pointlist[i], pointlist[j])

                    if dist <= min:  # Update min_dist and points
                        min = dist
                        point1, point2 = pointlist[i], pointlist[j]
                        distDict[(point1, point2)] = {'Dist': min}
        return min, point1, point2


def main():

    # file = "unsorted_10_2.txt"
    # numOfPoints, points = file_len_list(file)
    # minList = brute_force(points)
    # min = minList[-1][0]
    # print min
    # for i in reversed(minList):
    #     if i[0] <= min:
    #         print i[1:]

    if __name__ == "__main__":
        main()
