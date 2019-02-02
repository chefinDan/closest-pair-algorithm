# Author: Daniel Green, greendan@oregonstate.edu

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
    minlist = []

    with open(filename, 'r') as file:
        # p1 is x coord, p2 is y coord
        for point in file:
            p1 = int(point.strip().split(' ')[0])
            p2 = int(point.strip().split(' ')[1])
            plist.append((p1, p2))

    xsorted = sort_rands_on_x(plist)

    final = closest_pair(xsorted, distObj)

    #final = brute_force(plist, distObj)

    print final.getDistance()
    for i in final.getPoints():
        print (i)
    return

def closest_cross_pair(xlist, delta):
    distObj = Distance.Distance()
    length = int(len(xlist))
    mid = int(length//2)
    if length < 7:
        strip = xlist
    else:
        strip = xlist[(int(math.floor(mid-delta))):(int(math.ceil(mid+delta))+1)]
    strip = sort_rands_on_y(strip)
    index = 0
    # constant 7*n time
    for point in strip:
        for i in range (1,8):
            if index + i < len(strip):
                distObj.safeAddPoints(point, strip[index+i])
        index += 1

    return distObj



def closest_pair(xlist, distObj):
    length = len(xlist)
    index = 0
    if(length <= 3):
        for point in xlist:
            if index + 1 < len(xlist):
                distObj.safeAddPoints(point, xlist[index+1])
            index += 1
        return distObj

    mid = length // 2
    leftArrayX = xlist[:mid]
    rightArrayX = xlist[mid:]


    distObj1 = closest_pair(leftArrayX, distObj)
    distObj2 = closest_pair(rightArrayX, distObj)

    distObj1.combine(distObj2)
    delta = distObj1.getDistance()


    min_cross = closest_cross_pair(xlist, delta)

    return distObj1.combine(min_cross)


if(__name__ == "__main__"):
    main()
