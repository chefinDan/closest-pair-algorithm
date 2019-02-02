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

    #final = closest_pair(xsorted, distObj)

    final = brute_force(plist, distObj)

    print final.getDistance()
    for i in final.getPoints():
        print (i)
    return


if(__name__ == "__main__"):
    main()