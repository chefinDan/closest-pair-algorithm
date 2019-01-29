import random

def main():
    for power in range(2, 6):
        templist = []
        for x in range(0,10 ** power):
            pair = str(random.randint(0, 10 ** power)) + " " + str(random.randint(0, 10 ** power)) + "\n"
            templist.append(pair)
        sort = sorted(templist, key = toInt)
        filename = "random_10_" + str(power) + ".txt"
        with open(filename, "w") as fp:
            for line in sort:
                fp.write(line)


def toInt(line):
    return int(line.split(" ")[0])

if __name__ == '__main__':
    main()
