import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]

PART_1, PART_2 = 0, 0

WIN = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

DRAW = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

LOSE = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


def rock_paper_scissors(data):
    global PART_1
    for line in data:
        player_one, player_two = line.split()
        if WIN[player_one] == player_two:
            PART_1 += SCORE[player_two] + 6
        elif DRAW[player_one] == player_two:
            PART_1 += SCORE[player_two] + 3
        else:
            PART_1 += SCORE[player_two]

def rock_paper_scissors_part_two(data):
    global PART_2
    for line in data:
        player_one, end = line.split()
        if end == "X":
            player_two = LOSE[player_one]
            PART_2 += SCORE[player_two]
        if end == "Y":
            player_two = DRAW[player_one]
            PART_2 += SCORE[player_two] + 3
        if end == "Z":
            player_two = WIN[player_one]
            PART_2 += SCORE[player_two] + 6

rock_paper_scissors(PUZZLE)
rock_paper_scissors_part_two(PUZZLE)

print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")
        