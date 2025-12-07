

input_file = 'input.txt'
input_data = open(input_file).read()

manifold = [list(s) for s in input_data.split('\n')]

def PrintManifold():
    s = ""
    for line in manifold:
        for ch in line:
            s = s + ch
        s = s + "\n"
    print(s)



startX = -1
startY = -1
for y, line in enumerate(manifold):
    for x, ch in enumerate(line):
        if(ch == 'S'):
            startX = x
            startY = y
            break;
    if(startX != -1):
        break

beamPositions = [(startX, startY)]

#PrintManifold()
it = 0
splitCount = 0
while(True):
    newBeamPosition = []
    for i, pos in enumerate(beamPositions):
        x, y = pos
        if(manifold[y + 1][x] == '.'):
            manifold[y + 1][x] = '|'
            newBeamPosition.append((x, y + 1))
            continue
        if(manifold[y + 1][x] == '^'):
            manifold[y + 1][x + 1] = '|'
            manifold[y + 1][x - 1] = '|'
            newBeamPosition.append((x + 1, y + 1))
            newBeamPosition.append((x - 1, y + 1))
            splitCount = splitCount + 1
            continue
    beamPositions = newBeamPosition
    # PrintManifold()
    it = it + 1
    # if(it == 5):
    #     break

    if(len(beamPositions) == 0):
        break
    x, y = beamPositions[0]
    if(y + 1 >= len(manifold)):
        break

PrintManifold()
print(splitCount)


