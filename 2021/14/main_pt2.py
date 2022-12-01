import math
data = open("input.txt", 'r').readlines()
template = data[0].rstrip()
pairDict = {i[:2]:i[-2] for i in data[2:]}
count = {i:template.count(i) for i in pairDict.keys()}

for step in range(0, 40):
    countCopy = count.copy()
    for k, v in count.items():
        if count[k] > 0:
            countCopy[k] -= v
            countCopy[k[0] + pairDict[k]] += v
            countCopy[pairDict[k] + k[1]] += v
    count = countCopy

charCounts = {x:0 for x in set(''.join(count.keys()))}

for k, v in count.items():
    charCounts[k[0]] += v/2
    charCounts[k[1]] += v/2

answerFloat = max(charCounts.values()) - min(charCounts.values())
print(math.ceil(answerFloat))
