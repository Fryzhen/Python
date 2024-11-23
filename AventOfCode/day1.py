import re

def part1():
    with open("day1.txt") as f:
        data = f.read().split("\n")
        i = 0
        for line in data:
            num = str(re.sub("[^0-9]", "", line))
            i += int(num[0] + num[-1])
        print(i)

def part2():
    with open("day1.txt") as f:
        data = f.read().split("\n")
        i = 0
        for line in data:
            num = str(re.sub("[^0-9]", "", line))
            i += int(num[0] + num[-1])
        print(i)



if __name__ == "__main__":

