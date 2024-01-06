import math

with open("6ainput.txt") as f:
    def calculate_viable_range(time, distance):
        temp = math.sqrt((math.pow(time, 2) / 4) - distance)
        smallest = max(math.ceil((time / 2) - temp), 0)
        largest = min(math.floor((time / 2) + temp), time)

        return largest - smallest + 1
    
    lines = f.readlines()
    times = map(int, lines[0].split(":")[1].strip().split())
    distances = map(int, lines[1].split(":")[1].strip().split())

    total = 1
    for time, distance in zip(times, distances):
        total *= calculate_viable_range(time, distance)

    print(total)
