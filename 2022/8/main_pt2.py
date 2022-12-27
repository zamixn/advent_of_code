input_file = 'input.txt'

trees = [[int(x) for x in line] for line in open(input_file).read().split('\n')]

scenicScores = []

for y in range(0, len(trees)):
    for x in range(0, len(trees[0])):
        index = (x, y)

        visibleUp = 0        
        visibleDown = 0
        visibleLeft = 0
        visibleRight = 0

        for yy in range(y - 1, -1, -1): # top
            visibleUp += 1
            if trees[yy][x] >= trees[y][x]:
                break;

        for yy in range(y + 1, len(trees)): # down
            visibleDown += 1
            if trees[yy][x] >= trees[y][x]:
                break;

        for xx in range(x - 1, -1, -1): # left
            visibleLeft += 1
            if trees[y][xx] >= trees[y][x]:
                break;

        for xx in range(x + 1, len(trees[0])): # right
            visibleRight += 1
            if trees[y][xx] >= trees[y][x]:
                break;

        scenicScores.append(visibleDown * visibleLeft * visibleRight * visibleUp)

print(max(scenicScores))