with open("5ainput.txt") as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        if i == 0:
            old_set = set(map(int, lines[0].split(":")[1].strip().split(" ")))
        elif i == 1:
            continue
        elif "map" in line:
            new_set = set()
            new_mappings = []
        elif len(line.strip()) == 0:
            for old_num in old_set:
                for smallest, largest, difference in new_mappings:
                    if smallest <= old_num <= largest:
                        new_set.add(old_num + difference)
                else:
                    new_set.add(old_num)
            old_set = new_set
        else:
            a, b, c = map(int, line.strip().split(" "))
            smallest = b
            largest = b + c - 1
            difference = a - b
            new_mappings.append([smallest, largest, difference])

    print(min(old_set))