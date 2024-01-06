transitions = {}

with open("8ainput.txt") as f:
    current_positions = set()

    def is_starting_position(position):
        return position[-1] == 'A'
    
    def is_ending_position(position):
        return position[-1] == 'Z'
    
    def are_all_positions_ending(positions):
        return all(map(is_ending_position, positions))
    
    def make_single_transition(position):
        return transitions[position, sequence[nr_steps % len(sequence)]]

    for i, line in enumerate(f.readlines()):
        if i == 0:
            sequence = list(line.strip())
        elif i == 1:
            continue
        else:
            start, left, right = ''.join(filter(lambda ch: ch not in "(),=", line)).split()
            transitions[start, 'L'] = left
            transitions[start, 'R'] = right

            if is_starting_position(start):
                current_positions.add(start)

    nr_steps = 0
    
    while True:
        if are_all_positions_ending(current_positions):
            break
        else:
            current_positions = set(map(make_single_transition, current_positions))
            nr_steps += 1

    print(nr_steps)
    