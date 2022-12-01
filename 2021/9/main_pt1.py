fileLines = open("input.txt", 'r').readlines()
data = [[int(height) for height in line.rstrip()] for line in fileLines]

def CellCheck(data, y, x, maxY, maxX):
    if ((x == maxX or data[y][x] < data[y][x + 1]) and 
        (x == 0    or data[y][x] < data[y][x - 1]) and 
        (y == maxY or data[y][x] < data[y + 1][x]) and 
        (y == 0    or data[y][x] < data[y - 1][x])):
        return True
    return False

lowpoints = []
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if (CellCheck(data, y, x, len(data) - 1, len(data[y]) - 1)):
            lowpoints.append(data[y][x])

print(sum([p + 1 for p in lowpoints]))