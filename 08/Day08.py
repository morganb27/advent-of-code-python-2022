import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, float("-inf")

def treetop(data):
    global PART_1, PART_2
    rowNum, colNum = len(data), len(data[0])
    for row in range(len(data)):
        for col in range(len(data[row])):
            if isTreeVisible(data, data[row][col], row, col, rowNum, colNum):
                PART_1 += 1
            PART_2 = max(PART_2, calculateScenicScore(data, data[row][col], row, col, rowNum, colNum))


def isTreeVisible(data, tree, row, col, rowNum, colNum):
    if row == 0 or row == rowNum - 1 or col == 0 or col == colNum - 1:
        return True
    elif all(tree > data[row][j] for j in range(col)) or all(tree > data[row][j] for j in range(col + 1, colNum)):
        return True
    elif all(tree > data[i][col] for i in range(row)) or all(tree > data[i][col] for i in range(row + 1, rowNum)):
        return True

def calculateScenicScore(data, tree, row, col, rowNum, colNum):
    top, right, bottom, left = 0, 0, 0, 0
    for i in range(row - 1, -1, -1):
        if data[i][col] < data[row][col]:
            top += 1
        elif data[i][col] >= data[row][col]:
            top += 1
            break

    for j in range(col + 1, colNum):
        if data[row][j] < data[row][col]:
            right += 1
        elif data[row][j] >= data[row][col]:
            right += 1
            break
    
    for i in range(row + 1, rowNum):
        if data[i][col] < data[row][col]:
            bottom += 1
        elif data[i][col] >= data[row][col]:
            bottom += 1
            break
    
    for j in range(col - 1, -1, -1):
        if data[row][j] < data[row][col]:
            left += 1
        elif data[row][j] >= data[row][col]:
            left += 1
            break
    
    print(data[row][col], top, right, bottom, left)
    return top * right * bottom * left
    



treetop(PUZZLE)

print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")