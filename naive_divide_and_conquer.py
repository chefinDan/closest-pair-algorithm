from helpers import *
from brute_force import *
import sys
import math

def read_file(file):
	points = []
	with open(file) as f:
		for point_count, line in enumerate(f):
			points.append(line.strip())
	return point_count + 1, points

def closest_pair(points):
	length = len(points)
	mid = length//2
	print (length)
	if length <= 3:
		return brute_force(points)
	else:
		sortXarray = sortX(points)					#sort points by x
		midx = median(sortXarray)					#get the median x(middle point)
		print "mid", midx
		left = []
		right = []
		for x in sortXarray:						#get all the points with x smaller than median on the
			if x[0] <= midx:						#left, bigger on the right			
				left.append(x)
			else:
				right.append(x)
		leftArray = closest_pair(left)				#recursive call
		rightArray = closest_pair(right)
		minLeft = leftArray[0][0]					#get the min distance on left side
		minRight = rightArray[0][0]					#get the min distance on right side
		min = min_distance(minLeft, minRight)		#get the smaller distance
		delta1 = min + midx							#get the range of middle set
		delta2 = midx - min
		merge_array = leftArray.append(rightArray)	#merge left and right arrays
		M = []
		for x in merge_array:						#get all points that fall in middle into M
			if x[1] >= delta2 and x[1] <= delta1:
				M.append(x)
		sortedlist = sortY(M)						#sort them by Y in increasing order
		print "left", left
		print "right", right
		print "left", left
		print "right", right
	return
	
def sortY(list):
	return sorted(list , key=lambda k: [k[1], k[0]])
def sortX(list):
	return sorted(list, key=lambda k: k[0])
		
def median(points):
	length = len(points)
	index = length//2
	if length % 2:
		return points[index][0]
	else:
		return (int(points[index][0]) + int(points[index + 1][0]))/2

def main():
	points = []
	name = sys.argv[1]
	with open(name, 'r') as filename:
		for point in filename:
			p1 = int(point.strip().split(' ')[0])
			p2 = int(point.strip().split(' ')[1])
			points.append((p1,p2))

	minimum = closest_pair(points)
	return minimum
	
	
if __name__ == '__main__':
	main()

	