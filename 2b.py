from functools import reduce
import operator

total = 0

with open("2binput.txt") as f:
    for line in f.readlines():
        split1 = line.split(":")

        min_values = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        for picked_set in split1[1].split(";"):
            for value_colour in picked_set.split(","):
                value, colour = value_colour.strip().split(" ")
                min_values[colour] = max(min_values[colour], int(value))

        total += reduce(operator.mul, min_values.values(), 1)

print(total)