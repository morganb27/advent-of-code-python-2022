import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1 = 0

def treetop(data):
    global PART_1
    rowNum, colNum = len(data), len(data[0])
    for row in range(len(data)):
        for col in range(len(data[row])):
            if isTreeVisible(data, data[row][col], row, col, rowNum, colNum):
                PART_1 += 1

def isTreeVisible(data, tree, row, col, rowNum, colNum):
    if row == 0 or row == rowNum - 1 or col == 0 or col == colNum - 1:
        return True
    elif all(tree > data[row][j] for j in range(col)) or all(tree > data[row][j] for j in range(col + 1, colNum)):
        return True
    elif all(tree > data[i][col] for i in range(row)) or all(tree > data[i][col] for i in range(row + 1, rowNum)):
        return True
    



treetop(PUZZLE)

print(f"Solution to part 1 is: {PART_1}")