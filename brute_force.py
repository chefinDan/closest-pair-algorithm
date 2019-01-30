# Author: Daniel Green, greendan@oregonstate.edu
#
# Usage: put the helpers.py file in the same directory as this file.
# change string var "file" to be whichever file you want to run.
#

 
from helpers import *
import sys

def file_len_list(file_name):
    points = []
    with open(file_name) as f:
        for point_count, line in enumerate(f):
            points.append(line.strip())
    return point_count + 1, points

def brute_force(plist):
    minList = [] # will be list of tuples (min, point 1, point 2)
    ln = len(plist)
    min = point_dist(plist[0], plist[1]) # just use the first set of points as the min dist
    ln = len(plist)

    if ln == 2: # with 2 points the min is there distance
        minList.append((min, plist[0], plist[1]))
        return minList

    for i in range(ln-1):
        for j in range(i + 1, ln): # range of j gets smaller as we traverse list

            if i != 0 and j != 1: # if the end of the list has not been reached
                dist = point_dist(plist[i], plist[j])

                if dist <= min:  # Update min_dist and points
                    minList.append((dist, plist[i], plist[j]))
                    min, p1, p2 = dist, plist[i], plist[j]
    return minList

def main():

    file = "Testing Cases/random_10_3.txt"
    numOfPoints, points = file_len_list(file)
    minList = brute_force(points)
    min = minList[-1][0]
    print min
    for i in reversed(minList):
        if i[0] <= min:
            print i[1:]

if __name__ == "__main__":
    main()