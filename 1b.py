total = 0

numbers_dict = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

with open("1binput.txt") as f:
    for line in f.readlines():
        replaced_line = line
        for word, number in numbers_dict.items():
            replaced_line = replaced_line.replace(word, number)
        
        integers = list(map(int, filter(lambda x: x.isdigit(), list(replaced_line))))
        total += integers[0] * 10 + integers[-1]

print(total)