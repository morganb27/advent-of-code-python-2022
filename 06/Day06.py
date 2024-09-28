import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = None, None

def tuning_trouble(data):
    global PART_1, PART_2
    for line in data:
        print(line)
        PART_1 = find_start_of_packer_marker(line)
        PART_2 = find_start_of_message_packet(line)

def find_start_of_packer_marker(line):
    for i in range(len(line[:-3])):
        subroutine = line[i: i+4]
        print(subroutine)
        if len(subroutine) == len(set(subroutine)):
            return i + 4
        
def find_start_of_message_packet(line):
    for i in range(len(line[:-13])):
        subroutine = line[i: i+14]
        print(subroutine)
        if len(subroutine) == len(set(subroutine)):
            return i + 14


tuning_trouble(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")