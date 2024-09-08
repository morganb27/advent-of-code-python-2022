import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, 0
ELVES = []
CALORIES = 0

def colorie_counting(data):
    global PART_1, PART_2, ELVES, CALORIES
    for i, item in enumerate(data):
        if item:
            CALORIES += int(item)
        else:
            ELVES.append(CALORIES)
            CALORIES = 0
    PART_1 = max(ELVES)
    PART_2 = sum(sorted(ELVES, reverse=True)[:3])
        

colorie_counting(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")