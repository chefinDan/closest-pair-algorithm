from helpers import *
from brute_force import *
import sys

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
		M = []
		sortedList = []
		left = []
		right = []
		midx = points[mid][0]
		for x in points:
			if x[0] <= midx:
				left.append(x)
			else:
				right.append(x)
				
		minlist1 = closest_pair(left)
		minlist2 = closest_pair(right)
		for i in range(length):
			x = get_x(points[i])
			if x < max and x > min:
				M.append(points[i])
		#sortedList = sortY(points)
		print "left", minlist1
		print "right", minlist2
	return
	
def sortY(list):
	length = len(list)
	print length
	for i in range(length):
		min = list[i[1]]
		pos = i
		while pos < length and list[i+1[1]] > min:
			list[i[1]] = list[i+1[1]]
			pos = pos +1
		list[pos[1]]=min
	return list
		
		

def main():
	points_file = "Testing Cases/random_10_3.txt"
	num, points = read_file(points_file)
	min = closest_pair(points)
	
	
if __name__ == '__main__':
	main()

	