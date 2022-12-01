fileLines = open("input.txt", 'r').readlines()
data = [line.rstrip() for line in fileLines]

chunkOpeners = ['(','[','{','<']
chunkClosers = [')',']','}','>']
chunks = {'(':')', '[':']', '{':'}',  '<':'>'   }
points = {    ')':3,   ']':57,  '}':1197, '>':25137   }

pointsSum = 0
for line in data:
    openedChunks = []
    for c in line:
        if c in chunkOpeners:
            openedChunks.append(c)
        else:
            expected = chunks[openedChunks[-1]]
            if expected == c:
                del openedChunks[-1]
            else:
                pointsSum += points[c]
                break

print(pointsSum)