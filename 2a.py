total = 0

value_colour_dict = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

with open("2ainput.txt") as f:
    for line in f.readlines():
        split1 = line.split(":")
        game_nr = int(split1[0].split(" ")[-1])

        eligible = True
        for picked_set in split1[1].split(";"):
            for value_colour in picked_set.split(","):
                value, colour = value_colour.strip().split(" ")
                if int(value) > value_colour_dict[colour]:
                    eligible = False

        if eligible:
            total += game_nr

print(total)