import math

with open("6ainput.txt") as f:
    def calculate_viable_range(time, distance):
        temp = math.sqrt((math.pow(time, 2) / 4) - distance)
        smallest = max(math.ceil((time / 2) - temp), 0)
        largest = min(math.floor((time / 2) + temp), time)

        return largest - smallest + 1
    
    lines = f.readlines()
    time = int(''.join(lines[0].split(":")[1].strip().split()))
    distance = int(''.join(lines[1].split(":")[1].strip().split()))

    print(calculate_viable_range(time, distance))
