import sys

def main():
    power = 0
    if len(sys.argv) == 2:
        try:
            power = int(sys.argv[1])
        except ValueError:
            print("Input is not an int")
            return
    else:
        print("Incorrect number of arguments")
        return
    
    
    if power > 5:
        print("Please input an integer less than or equal to 5")
        return

    filename = "random_10_" + str(power) + ".txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
        sort = sorted(lines, key = toInt)

    with open(filename, "w") as fp:
        for line in sort:
            fp.write(line)

    

def toInt(line):
    return int(line.split(" ")[0])

if __name__ == '__main__':
    main()
