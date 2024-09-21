import fileinput

INPUT = ''.join(fileinput.input())
BOARD, MOVES = INPUT.split('\n\n')
BOARD = BOARD.splitlines()
BOTTOM = BOARD[-1]
NUM_OF_STACKS = max(int(x) for x in BOTTOM.split())
STACKS = [[] for _ in range(NUM_OF_STACKS)]
PART_1 = ''


for line in BOARD[::-1]:
    for i, crate in enumerate(line[1::4]):
        if crate.isupper():
            STACKS[i].append(crate)

def supply_stacks(data):
    global PART_1
    for line in data.splitlines():
        x, y, z = parse_line(line)
        for _ in range(x):
            crate_to_move = STACKS[y - 1].pop()
            STACKS[z - 1].append(crate_to_move)
    
    for i in range(len(STACKS)):
        PART_1 += STACKS[i][-1]


def parse_line(line):
    numbers = [int(part) for part in line.split() if part.isdigit()]
    return numbers

supply_stacks(MOVES)

print(f"Solution to part 1 is: {PART_1}")