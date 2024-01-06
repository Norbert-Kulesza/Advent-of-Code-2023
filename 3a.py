total = 0

with open('3ainput.txt', 'r') as f:
    def is_character(x):
        return not x.isdigit() and x != '.'

    def has_adjacent_character(num_start_x, num_end_x, y):
        border_start_x = max(num_start_x - 1, 0)
        border_end_x = min(num_end_x + 1, width - 1)
        border_start_y = max(y - 1, 0)
        border_end_y = min(y + 1, height - 1)

        found = False
        for i in range(border_start_y, border_end_y + 1):
            for j in range(border_start_x, border_end_x + 1):
                if is_character(l[i][j]):
                    found = True
                    break

        return found
    
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
                    if has_adjacent_character(start_x, end_x, y):
                        total += current_char
            if not character.isdigit():
                if current_char != 0:
                    end_x = x - 1
                    if has_adjacent_character(start_x, end_x, y):
                        total += current_char
                    current_char = 0    

print(total)