import sys

def toInt(line):
    return int(line.split(" ")[0])

def sort_rands_on_y(plist):
    return sorted(plist, key=lambda tup: tup[1])

def sort_rands_on_x(plist):
    return sorted(plist, key=lambda tup: tup[0])
