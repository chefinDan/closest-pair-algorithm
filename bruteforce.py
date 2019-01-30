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
        for point_count, point in enumerate(f):
            points.append(point.strip())
    return point_count + 1, points


def brute_force(plist):
    # print "in brute force plist: ", plist
    minlist = [] # will be list of tuples (min, point 1, point 2)
    min = point_dist(plist[0], plist[1]) # just use the first set of points as the min dist
    # print "in brute frce min: ", min
    ln = len(plist)

    if (ln == 2):
        minlist.append((min, plist[0], plist[1]))
        return minlist
    else:
        for i in range(ln-1):
            for j in range(i + 1, ln): # range of j gets smaller as we traverse list

                if i != 0 and j != 1: # if the end of the list has not been reached
                    dist = point_dist(plist[i], plist[j])

                    if dist <= min:  # Update min_dist and points
                        minlist.append((dist, plist[i], plist[j]))
                        min, p1, p2 = dist, plist[i], plist[j]
                    else:
                        minlist.append((min, plist[0], plist[1]))
        return minlist

def main():

    file = "unsorted_10_2.txt"
    numOfPoints, points = file_len_list(file)
    minList = brute_force(points)
    min = minList[-1][0]
    print min
    for i in reversed(minList):
        if i[0] <= min:
            print i[1:]

if __name__ == "__main__":
    main()
