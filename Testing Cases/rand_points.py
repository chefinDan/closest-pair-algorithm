import sys
import random

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

    fp = open(filename, "w")

    for x in range(0,10 ** power):
        pair = str(random.randint(0, 10 ** power)) + " " + str(random.randint(0, 10 ** power))
        fp.write(pair)
        fp.write("\n")

    fp.close()

    
if __name__ == '__main__':
    main()
