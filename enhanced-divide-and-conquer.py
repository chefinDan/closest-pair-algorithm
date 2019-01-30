# Author: Daniel Green, greendan@oregonstate.edu


import sys
from helpers import *
from sort_rands import *
from bruteforce import *

def main():

    plist = []
    filename = sys.argv[1]

    with open(filename, 'r') as file:
        for point in file:
            p1 = int(point.strip().split(' ')[0])
            p2 = int(point.strip().split(' ')[1])
            plist.append((p1,p2))

    length = len(plist)
    xsorted = sort_rands_on_x(plist)
    ysorted = sort_rands_on_y(plist)

    minimum = closest_pair(xsorted, ysorted)

    print minimum
    return minimum


def getmin(minlist):
    if len(minlist) == 1:
        return minlist

    min = minlist[-1][0]
    li = [min]

    for i in reversed(minlist):
        if i[0] == min:
            li.append(i[1:])
    return li

def closest_pair(xlist, ylist):
    length = len(xlist)
    if(length <= 3):
        return brute_force(xlist)

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

    minlist1 = closest_pair(leftArrayX, leftArrayY)
    minlist2 = closest_pair(rightArrayX, rightArrayY)

    if (minlist1 and minlist2):
        min1 = getmin(minlist1)
        min2 = getmin(minlist2)
        if min1[0][0] <= min2[0][0]:
            min = min1[0]
        else:
            min = min2[0]

    return [min]


if(__name__ == "__main__"):
    main()
