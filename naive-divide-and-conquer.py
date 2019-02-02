# Author: Daniel Green, Alex Lung
import sys
from sort_rands import *
from bruteforce import brute_force
from helpers import point_dist
import decimal
import math
import Distance


def main():
    filename = sys.argv[1]
    distObj = Distance.Distance()
    plist = []

    # make a list of tuples, where each entry in the list is a (x, y) tuple
    with open(filename, 'r') as file:
        for point in file:
            p1 = int(point.strip().split(' ')[0])
            p2 = int(point.strip().split(' ')[1])
            plist.append((p1, p2))

    # closest-pair returns a distance object, class def. found in Distance.py
    final = closest_pair(plist, distObj)

    print final.getDistance()
    for i in final.getPoints():
        print (i)
    return


def closest_cross_pair(xlist, delta):
    distObj = Distance.Distance()
    length = int(len(xlist))
    mid = xlist[length//2][0]

    # sort y points in each iteration
    ysorted = sort_rands_on_y(xlist)

    # strip is a list of y sorted points built by finding all x-coords that exist
    # within the boundries of the strip, ie mid - delta and mid + delta
    strip = [x for x in ysorted if mid - delta <= x[0] <= mid + delta]

    index = 0
    # constant 7*n time
    for point in strip:
        for i in range (1,8):
            if index + i < len(strip):
                distObj.safeAddPoints(point, strip[index+i])
        index += 1

    return distObj

# Recursive function closest_pair()
def closest_pair(plist, distObj):
    # sort list by x coord in each iteration
    xsorted = sort_rands_on_x(plist)
    length = len(xsorted)
    index = 0

    # if length of x-sorted array has 3 or less points, then brute-force compare
    # the points and return the min distance/points as a Distance object
    if(length <= 3):
        for point in xsorted:
            if index + 1 < len(xsorted):
                distObj.safeAddPoints(point, xsorted[index+1])
            index += 1
        return distObj

    mid = length // 2
    leftArrayX = xsorted[:mid]
    rightArrayX = xsorted[mid:]

    # Recursively call closest_pair on each half of the x-sorted array,
    # stopping when base case length<=3 is achieved
    distObj1 = closest_pair(leftArrayX, distObj)
    distObj2 = closest_pair(rightArrayX, distObj)
    distObj1.combine(distObj2)

    # determine delta by gettng the smallest distance returned by the recursion
    delta = distObj1.getDistance()

    # call constant time closest_cross_pair() to determine the smallest distance
    # in the middle strip between the left and right x-sorted arrays
    min_cross = closest_cross_pair(xsorted, delta)

    # return the smallest distance of all 3 options
    return distObj1.combine(min_cross)


if(__name__ == "__main__"):
    main()
