total = 0

with open("1ainput.txt") as f:
    for line in f.readlines():
        integers = list(map(int, filter(lambda x: x.isdigit(), list(line))))
        total += integers[0] * 10 + integers[-1]

print(total)