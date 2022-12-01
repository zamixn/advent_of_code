fileLines = open("input.txt", 'r').readlines()
fishes = [int(x) for x in fileLines[0].split(',')]
counts = {x:fishes.count(x) for x in range(0, 10)}

for day in range(0, 256):
    counts[9] += counts[0]
    counts[7] += counts[0]
    counts[0] = 0
    for i in range(0, 9):
        counts[i] += counts[i + 1]
        counts[i + 1] = 0

print(sum([counts[x] for x in range(0, 9)]))