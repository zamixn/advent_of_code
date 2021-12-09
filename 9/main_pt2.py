fileLines = open("input.txt", 'r').readlines()
data = [[int(height) for height in line.rstrip()] for line in fileLines]

def LowPointCheck(data, y, x, maxY, maxX):
    if ((x == maxX or data[y][x] < data[y][x + 1]) and 
        (x == 0    or data[y][x] < data[y][x - 1]) and 
        (y == maxY or data[y][x] < data[y + 1][x]) and 
        (y == 0    or data[y][x] < data[y - 1][x])):
        return True
    return False

def FloodFillCell(data, y, x, basins, maxY, maxX):
    if data[y][x] == 9 or basins[y][x] != -1:
        return -1

    if (x != maxX and (basins[y][x + 1] != -1)):
        return basins[y][x + 1] 
    if (x != 0    and (basins[y][x - 1] != -1)):
        return basins[y][x - 1] 
    if (y != maxY and (basins[y + 1][x] != -1)):
        return basins[y + 1][x] 
    if (y != 0    and (basins[y - 1][x] != -1)):
        return basins[y - 1][x] 
    return -1

index = 0
basins = [[-1 for x in y] for y in data]
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if (LowPointCheck(data, y, x, len(data) - 1, len(data[y]) - 1)):
            basins[y][x] = index
            index += 1

noCellFilled = False
while noCellFilled != True:
    noCellFilled = True
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            basinIndex = FloodFillCell(data, y, x, basins, len(data) - 1, len(data[y]) - 1)
            if basinIndex != -1:
                basins[y][x] = basinIndex
                noCellFilled = False    

flattenedBasins = []
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if basins[y][x] != -1:
            flattenedBasins.append(basins[y][x])

basinSizes = sorted([flattenedBasins.count(x) for x in set(flattenedBasins)], reverse=True)
print(basinSizes[0] * basinSizes[1] * basinSizes[2])