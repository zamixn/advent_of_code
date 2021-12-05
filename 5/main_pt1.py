fileLines = open("input.txt", 'r').readlines()
lines = [[list(map(int, points[0].split(','))), list(map(int, points[1].split(',')))] 
            for points in [fileLine.rstrip().split(' -> ') for fileLine in fileLines]]
filtered = list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], lines))

width = max(filtered, key=lambda i: max(i[0][0], i[1][0]))
width = max(width[0][0], width[1][0]) + 1
height = max(filtered, key=lambda i: max(i[0][1], i[1][1]))
height = max(height[0][1], height[1][1]) + 1
grid = [[0 for x in range(width)] for y in range(height)]

for line in filtered:
    if line[0][0] == line[1][0]:
        start = min(line[0][1], line[1][1])
        end = max(line[0][1], line[1][1])
        for y in range(start, end + 1):
            grid[y][line[0][0]] += 1
    else:
        start = min(line[0][0], line[1][0])
        end = max(line[0][0], line[1][0])
        for x in range(start, end + 1):
            grid[line[0][1]][x] += 1

sum = sum([sum(x >= 2 for x in row) for row in grid])
print (sum)