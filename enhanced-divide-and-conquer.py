# Author: Daniel Green, greendan@oregonstate.edu

import sys
from sort_rands import *
from bruteforce import brute_force


def main():
    filename = sys.argv[1]
    distDict = {}
    plist = []
    with open(filename, 'r') as file:
        for point in file:
            p1 = int(point.strip().split(' ')[0])
            p2 = int(point.strip().split(' ')[1])
            plist.append((p1, p2))

    xsorted = sort_rands_on_x(plist)
    ysorted = sort_rands_on_y(plist)

    min, p1, p2 = closest_pair(xsorted, ysorted, distDict)

    print min
    for key, value in distDict.iteritems():
        if value['Dist'] == min:
            print key

    return min, p1, p2


def getmin(minlist):
    if len(minlist) == 1:
        return minlist

    min = minlist[-1][0]
    li = [min]

    for i in reversed(minlist):
        if i[0] == min:
            li.append(i[1:])
    return li


def closest_pair(xlist, ylist, distDict):
    length = len(xlist)
    if(length <= 3):
        return brute_force(xlist, distDict)

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

    minDist1, pleft1, pleft2 = closest_pair(leftArrayX, leftArrayY, distDict)
    minDist2, pright1, pright2 = closest_pair(rightArrayX, rightArrayY, distDict)

    if minDist1 <= minDist2:
        return minDist1, pleft1, pleft2
    else:
        return minDist2, pright1, pright2


if(__name__ == "__main__"):
    main()
