## Helper functions for Implementation Assignment 1
import math

def main():
    #pointOne = "45678 709\n"
    #pointTwo = "78 56911\n"
    #print("distance = ")
    ## computes distance between any 2 points in the given .txt format
    #print(point_dist(pointOne, pointTwo))
    #print()
    #print("x1 = ")
    #print(get_x(pointOne))
    #print()
    #print("y1 = ")
    #print(get_y(pointOne))
    #print()
    #print("x diff = ")
    #print(x_diff(pointOne, pointTwo))
    #print()
    #print("y diff = ")
    #print(y_diff(pointOne, pointTwo))
    return
    

def point_dist(pt1, pt2):
    print(pt1)
    print(pt2)
    p1 = pt1.split(' ')
    p2 = pt2.split(' ')
    print ("p1: ", p1)
    print ("p2: ", p2)
    try:
        x1 = int(p1[0])
        y1 = int(p1[1])
        x2 = int(p2[0])
        y2 = int(p2[1])
    except ValueError:
        print("Type mismatch")
        return(0)

    return(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

#return the x coordinate of a string point
def get_x(pt):
    return int(pt.split(' ')[0])

#return the y coordinate of a string point
def get_y(pt):
    return int(pt.split(' ')[1])

#find the absolute x difference between 2 string points
def x_diff(pt1, pt2):
    p1_x = int(pt1.split(' ')[0])
    p2_x = int(pt2.split(' ')[0])
    return abs(p1_x - p2_x)

#find the absolute y difference between 2 string points
def y_diff(pt1, pt2):
    p1_y = int(pt1.split(' ')[1])
    p2_y = int(pt2.split(' ')[1])
    return abs(p1_y - p2_y)
	
#compares two distances and returns the smaller distance
def min_distance(d1, d2):
	if d1 > d2:
		return d2
	else:
		return d1

    
    

main()
