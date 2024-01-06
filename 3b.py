from collections import defaultdict

total = 0
star_positions = defaultdict(list)

with open('3binput.txt', 'r') as f:

    def update_star_position(num_start_x, num_end_x, y):
        border_start_x = max(num_start_x - 1, 0)
        border_end_x = min(num_end_x + 1, width - 1)
        border_start_y = max(y - 1, 0)
        border_end_y = min(y + 1, height - 1)

        for i in range(border_start_y, border_end_y + 1):
            for j in range(border_start_x, border_end_x + 1):
                if l[i][j] == '*':
                    star_positions[(i, j)].append(current_char)

    
    l = [list(line.strip()) for line in f]
    width = len(l[0])
    height = len(l)

    for y, line in enumerate(l):
        start_x = 0
        current_char = 0
        for x, character in enumerate(line):
            if current_char == 0:
                start_x = x
            if character.isdigit():
                current_char = current_char * 10 + int(character)
                if x == width - 1:
                    end_x = x
                    update_star_position(start_x, end_x, y)
            if not character.isdigit():
                if current_char != 0:
                    end_x = x - 1
                    update_star_position(start_x, end_x, y)
                    current_char = 0    

    for star_values in star_positions.values():
        if len(star_values) == 2:
            total += star_values[0] * star_values[1]

print(total)