# Author: Daniel Green, greendan@oregonstate.edu

import sys
from sort_rands import *
from bruteforce import brute_force
import decimal
import Distance


def main():
    filename = sys.argv[1]
    distObj = Distance.Distance()
    plist = []
    minlist = []

    with open(filename, 'r') as file:
        for point in file:
            p1 = int(point.strip().split(' ')[0])
            p2 = int(point.strip().split(' ')[1])
            plist.append((p1, p2))

    xsorted = sort_rands_on_x(plist)
    ysorted = sort_rands_on_y(plist)

    final = closest_pair(xsorted, ysorted, distObj)

    print final.getDistance()
    for i in final.getPoints():
        print i
    return

# def closest_cross_pair(xlist, ylist, delta, distObj):
#     length = int(len(xlist))
#     mid = int(length//2)
#     strip = xlist[int(mid-delta):int(mid+delta)]
#     return brute_force(strip, distObj)



def closest_pair(xlist, ylist, distObj):
    length = len(xlist)
    if(length <= 3):
        return brute_force(xlist, distObj)

    mid = length // 2
    leftArrayX = xlist[:mid]
    rightArrayX = xlist[mid:]

    midpoint = xlist[mid][0]
    leftArrayY = []
    rightArrayY = []

    for point in ylist:
        if point[0] <= midpoint:
            leftArrayY.append(point)
        else:
            rightArrayY.append(point)

    distObj1 = closest_pair(leftArrayX, leftArrayY, distObj)
    distObj2 = closest_pair(rightArrayX, rightArrayY, distObj)

    if distObj1.getDistance() < distObj2.getDistance():
        delta = distObj1.getDistance()
        min = distObj1
    else:
        delta = distObj2.getDistance()
        min = distObj2

    # the closest_cross_pair function goes here.
    # params: xlist, ylist, delta, ??

    if distObj1.getDistance() < distObj2.getDistance():
        return distObj1
    else:
        return distObj2


if(__name__ == "__main__"):
    main()
