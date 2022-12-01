import math
fileLines = open("input.txt", 'r').readlines()
lines = [[list(map(int, points[0].split(','))), list(map(int, points[1].split(',')))] 
            for points in [fileLine.rstrip().split(' -> ') for fileLine in fileLines]]

width = max(lines, key=lambda i: max(i[0][0], i[1][0]))
width = max(width[0][0], width[1][0]) + 1
height = max(lines, key=lambda i: max(i[0][1], i[1][1]))
height = max(height[0][1], height[1][1]) + 1
grid = [[0 for x in range(width)] for y in range(height)]

for line in lines:
    if line[0][0] == line[1][0]:
        start = min(line[0][1], line[1][1])
        end = max(line[0][1], line[1][1])
        for y in range(start, end + 1):
            grid[y][line[0][0]] += 1
    elif line[0][1] == line[1][1]:
        start = min(line[0][0], line[1][0])
        end = max(line[0][0], line[1][0])
        for x in range(start, end + 1):
            grid[line[0][1]][x] += 1
    else:
        dirX = int(math.copysign(1, line[0][0] - line[1][0]))
        dirY = int(math.copysign(1, line[0][1] - line[1][1]))
        length = abs(line[0][0] - line[1][0])
        x = line[1][0]
        y = line[1][1]
        for i in range(length + 1):
            grid[y][x] += 1            
            x += dirX
            y += dirY

sum = sum([sum(x >= 2 for x in row) for row in grid])
print (sum)