transitions = {}

with open("8ainput.txt") as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            sequence = list(line.strip())
        elif i == 1:
            continue
        else:
            start, left, right = ''.join(filter(lambda ch: ch not in "(),=", line)).split()
            transitions[start, 'L'] = left
            transitions[start, 'R'] = right

    nr_steps = 0
    current_position = 'AAA'
    while True:
        if current_position == 'ZZZ':
            break
        else:
            current_position = transitions[current_position, sequence[nr_steps % len(sequence)]]
            nr_steps += 1

    print(nr_steps)

    