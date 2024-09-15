import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, 0


def camp_cleanup(data):
    global PART_1, PART_2
    for line in data:
        start_one, end_one, start_two, end_two = parse_input(line)
        if start_one <= start_two and end_one >= end_two:
            PART_1 += 1
        elif start_one >= start_two and end_one <= end_two:
            PART_1 += 1

        if end_one >= start_two and start_one <= start_two:
            PART_2 += 1
        elif end_two >= start_one and start_two <= start_one:
            PART_2 += 1
        


def parse_input(line):
    elf_one, elf_two = line.split(",")
    start_one, end_one = map(int, elf_one.split("-"))
    start_two, end_two = map(int, elf_two.split("-"))
    return start_one, end_one, start_two, end_two


camp_cleanup(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")