import math
isTest = 0
input_file = 'input.txt' if isTest == 0 else 'input_test.txt'
input_data = open(input_file)

points = [tuple(map(int, line.split(","))) for line in input_data]
pointsCount = len(points)

pointPairsToExclude = []
circuits = []

def FindCircuit(i):
    for circuitIndex, c in enumerate(circuits):
        for pIndexInCircuit in c:
            if(pIndexInCircuit == i):
                return (circuitIndex, c)
    return False

def ConnectPoints(i, j):
    iResult = FindCircuit(i)
    if(iResult == False):
        jResult = FindCircuit(j)
        if(jResult == False):
            # no circuits
            circuits.append([i, j])
        else:
            # i not found, j found
            jCircuitIndex, jCircuit = jResult
            jCircuit.append(i)
    else:
        iCircuitIndex, iCircuit = iResult
        jResult = FindCircuit(j)
        if(jResult == False):
            # i found, j not found
            iCircuit.append(j)
        else:
            # i found, j found
            jCircuitIndex, jCircuit = jResult
            for jPointIndex in jCircuit:
                iCircuit.append(jPointIndex)
            circuits.pop(jCircuitIndex)
    
def AreInSameCircuit(i, j):
    iResult = FindCircuit(i)
    if(iResult == False):
        return False
    jResult = FindCircuit(j)
    if(jResult == False):
        return False
    
    iIndex, iCircuit = iResult
    jIndex, jCircuit = jResult
    return iIndex == jIndex
        
def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distSquared = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
    return math.sqrt(distSquared)

distances = []
for i, p in enumerate(points):
    if(i >= pointsCount - 1):
        break
    shortestDistToI = math.inf
    shortestDistToIIndex = -1
    for j in range(i + 1, pointsCount):
        p2 = points[j]
        dist = distance(p, p2)
        distances.append((i, j, dist))
distances.sort(key=lambda t: t[2])

lastPair = (-1, -1)
for d in distances:
    i, j, dist = d

    p1 = points[i]
    p2 = points[j]
    if(AreInSameCircuit(i, j) == False):
        print("connecting:", i, "and", j, "(", p1, p2, ")")
        ConnectPoints(i, j)
    else:
        print("already connected:", i, "and", j, "(", p1, p2, ")")
    pointPairsToExclude.append((min(i, j), max(i, j)))

    print("circuits:", circuits)
    print(" ")

    allPointsInSameCircuit = True
    for index in range(0, pointsCount):
        if(AreInSameCircuit(0, index) == False):
            allPointsInSameCircuit = False
            break
    if(allPointsInSameCircuit == True):
        print("Last pair of connected points:", p1, p2)
        lastPair = (p1, p2)
        break

result = lastPair[0][0] * lastPair[1][0]
print(result)