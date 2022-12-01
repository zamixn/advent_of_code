fileLines = open("input.txt", 'r').readlines()
data = [line.rstrip() for line in fileLines]

chunkOpeners = ['(','[','{','<']
chunkClosers = [')',']','}','>']
chunks = {'(':')', '[':']', '{':'}',  '<':'>'   }
points = {    ')':1,   ']':2,  '}':3, '>':4   }

pointSums = []
for line in data:
    openedChunks = []
    corruptedLine = False
    for c in line:
        if c in chunkOpeners:
            openedChunks.append(c)
        else:
            expected = chunks[openedChunks[-1]]
            if expected == c:
                del openedChunks[-1]
            else:
                corruptedLine = True
                break

    if corruptedLine == False:
        closersNeeded = [chunks[x] for x in openedChunks[::-1]] 
        stringScore = "".join(closersNeeded)
        score = 0
        for c in stringScore:
            score = score * 5 + points[c]
        pointSums.append(score)

print(sorted(pointSums)[int(len(pointSums) / 2)])