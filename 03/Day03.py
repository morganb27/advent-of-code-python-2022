import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, 0

def rucksack_reorganization(data):
    global PART_1, PART_2
    for rucksack in data:
        PART_1 += common_item(rucksack)

    for i in range(0, len(data), 3):
        PART_2 += common_item_part_two(data[i], data[i+1], data[i+2])



def common_item(rucksack):
    item = None
    half = len(rucksack)//2
    left, right = rucksack[:half], rucksack[half:]
    for char in left:
        if char in right:
            item = char
            break
    return get_priority_part_two(item)
    

def common_item_part_two(first, second, third):
    for char in first:
        if char in second and char in third:
            return get_priority_part_two(char)

def get_priority_part_two(char):
    if char == char.lower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27
    
rucksack_reorganization(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")