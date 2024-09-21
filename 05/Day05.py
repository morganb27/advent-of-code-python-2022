import fileinput
import copy

INPUT = ''.join(fileinput.input())
BOARD, MOVES = INPUT.split('\n\n')
BOARD = BOARD.splitlines()
BOTTOM = BOARD[-1]
NUM_OF_STACKS = max(int(x) for x in BOTTOM.split())
STACKS = [[] for _ in range(NUM_OF_STACKS)]


for line in BOARD[::-1]:
    for i, crate in enumerate(line[1::4]):
        if crate.isupper():
            STACKS[i].append(crate)

def supply_stacks(data, part_two = False):
    stack = copy.deepcopy(STACKS)
    for line in data.splitlines():
        x, y, z = parse_line(line)
        crates_to_move = []

        if not part_two:
            for _ in range(x):
                crate_to_move = stack[y - 1].pop()
                stack[z - 1].append(crate_to_move)
        
        else:
            for _ in range(x):
                crate_to_move = stack[y - 1].pop()
                crates_to_move.append(crate_to_move)
            crates_to_move.reverse()
            stack[z - 1].extend(crates_to_move)
    return ''.join(s[-1] for s in stack if s)



def parse_line(line):
    numbers = [int(part) for part in line.split() if part.isdigit()]
    return numbers



print(f"Solution to part 1 is: {supply_stacks(MOVES)}")
print(f"Solution to part 2 is: {supply_stacks(MOVES, True)}")