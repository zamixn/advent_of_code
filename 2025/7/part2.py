from collections import defaultdict

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

def PrintBeamValues(beams):
    s = [str(val) + " " for x, y, val in beams]
    print("".join(s))

def RemoveBeamByPositionAndReturnValue(beams, x, y):
    indexToRemove = -1
    value = 0
    for i, b in enumerate(beams):
        bx, by, val = b
        if(bx == x and by == y):
            indexToRemove = i
            value = val
            break
    beams.pop(indexToRemove)
    return value

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

beams = [(startX, startY, 1)]

while(True):
    newBeams = []
    for i, beam in enumerate(beams):
        x, y, val = beam
        if(manifold[y + 1][x] == '.'):
            manifold[y + 1][x] = '|'
            newBeams.append((x, y + 1, val))
            continue

        elif(manifold[y + 1][x] == '^'):
            if(manifold[y + 1][x + 1] == '.'):
                manifold[y + 1][x + 1] = '|'
                newBeams.append((x + 1, y + 1, val))
            else:
                oldValue = RemoveBeamByPositionAndReturnValue(newBeams, x + 1, y + 1)
                newBeams.append((x + 1, y + 1, oldValue + val))

            if(manifold[y + 1][x - 1] == '.'):
                manifold[y + 1][x - 1] = '|'
                newBeams.append((x - 1, y + 1, val))
            else:
                oldValue = RemoveBeamByPositionAndReturnValue(newBeams, x - 1, y + 1)
                newBeams.append((x - 1, y + 1, oldValue + val))
            continue

        elif (manifold[y + 1][x] == '|'):
            oldValue = RemoveBeamByPositionAndReturnValue(newBeams, x, y + 1)
            newBeams.append((x, y + 1, oldValue + val))
            continue

    beams = newBeams

    if(len(beams) == 0):
        break
    x, y, val = beams[0]
    if(y + 1 >= len(manifold)):
        break

PrintManifold()
totalTimelines = 0
for beam in beams:
    x, y, val = beam
    totalTimelines = totalTimelines + val  
PrintBeamValues(beams)
print(totalTimelines)

