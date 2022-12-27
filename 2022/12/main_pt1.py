def GetElavation(c):
    if c == 'S': c = 'a'
    if c == 'E': c = 'z'
    return ord(c) - ord('a')

def PrintMap(map):
    for i in range(0, len(map)):
        line = map[i]
        s = ''
        for c in line:
            s += f' {c[0]}-{GetElavation(c[0]): <4}|'
        s += '\n'
        for c in line:
            s += f'  {c[1]: <5}|'
        s += '\n' + ('_' * len(line) * 8)
        print(s)

input_file = 'input.txt'
heightmap = [[(c, '.') for c in line] for line in open(input_file).read().split('\n')]

def FloodFillNeighbour(current, neighbour):
    if neighbour != None and GetElavation(current[0]) - 1 <= GetElavation(neighbour[0]) and neighbour[1] != '.':
        candidate = (current[0], neighbour[1] + 1)
        return candidate if current[1] == '.' or current[1] > candidate[1] else current
    else:
        return current


goalReached = False
while not goalReached:
    for y in range(0, len(heightmap)):
        for x in range(0, len(heightmap[0])):
            c = heightmap[y][x][0]
            s = heightmap[y][x][1]

            leftNeighbour = heightmap[y][x-1] if x > 0 else None
            rightNeighbour = heightmap[y][x+1] if x < len(heightmap[y]) - 1 else None
            upNeighbour = heightmap[y-1][x] if y > 0 else None
            downNeighbour = heightmap[y+1][x] if y < len(heightmap) - 1 else None

            if c == 'S':
                heightmap[y][x] = (c, 0)
            
            if s == '.':
                heightmap[y][x] = FloodFillNeighbour(heightmap[y][x], leftNeighbour)
                heightmap[y][x] = FloodFillNeighbour(heightmap[y][x], rightNeighbour)
                heightmap[y][x] = FloodFillNeighbour(heightmap[y][x], upNeighbour)
                heightmap[y][x] = FloodFillNeighbour(heightmap[y][x], downNeighbour)

                c = heightmap[y][x][0]
                s = heightmap[y][x][1]

                if c == 'E' and s != '.':
                    goalReached = True
                    print(s)


#PrintMap(heightmap)
