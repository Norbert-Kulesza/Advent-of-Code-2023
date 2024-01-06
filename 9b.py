import math

total = 0

with open("9ainput.txt") as f:

    def get_sequence_from_input(line):
        return list(map(int, line.strip().split()))

    def are_all_zeros(sequence):
        return all([x == 0 for x in sequence])
    
    def generate_all_sequences(sequence):
        sequences = [sequence]

        while not are_all_zeros(sequences[-1]):
            last_sequence = sequences[-1]
            next_sequence = []
            for i in range(len(last_sequence) - 1):
                next_sequence.append(last_sequence[i + 1] - last_sequence[i])
            sequences.append(next_sequence)

        return sequences

    def get_previous_value(sequence):
        sequences = generate_all_sequences(sequence)
        next_value = sum([sequence[0] * int(math.pow(-1, i)) for i, sequence in enumerate(sequences)])

        return next_value

    for line in f.readlines():
        sequence = get_sequence_from_input(line)
        total += get_previous_value(sequence)

    print(total)
    