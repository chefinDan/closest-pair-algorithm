import random

def main():
    for power in range(2, 6):
        templist = []
        x_avail = range(0, 10**power)
        for x in range(0,10 ** power):
            x = random.choice(x_avail)
            x_avail.remove(x)
            y = random.randint(0, 10 ** power)
            pair = str(x) + " " + str(y) + "\n"
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
