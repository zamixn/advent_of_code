input_file = 'input.txt'

trees = [[int(x) for x in line] for line in open(input_file).read().split('\n')]

visibleTreeIndexes = []

for y in range(0, len(trees)):
    for x in range(0, len(trees[0])):
        index = (x, y)
        if index in visibleTreeIndexes:
            continue
        if y == 0 or y == len(trees) - 1 or x == 0 or x == len(trees[0]) - 1:            
            visibleTreeIndexes.append(index)
            continue

        visible = True
        for yy in range(0, y): # top
            if trees[yy][x] >= trees[y][x]:
                visible = False;
                break;
        
        if visible:           
            visibleTreeIndexes.append(index)
            continue

        visible = True
        for yy in range(y + 1, len(trees)): # down
            if trees[yy][x] >= trees[y][x]:
                visible = False;
                break;
        
        if visible:           
            visibleTreeIndexes.append(index)
            continue

        visible = True
        for xx in range(0, x): # left
            if trees[y][xx] >= trees[y][x]:
                visible = False;
                break;
        
        if visible:           
            visibleTreeIndexes.append(index)
            continue

        visible = True
        for xx in range(x + 1, len(trees[0])): # right
            if trees[y][xx] >= trees[y][x]:
                visible = False;
                break;
        
        if visible:           
            visibleTreeIndexes.append(index)
            continue



print(len(visibleTreeIndexes))
