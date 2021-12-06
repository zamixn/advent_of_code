fileLines = open("input.txt", 'r').readlines()
fishes = [int(x) for x in fileLines[0].split(',')]

for day in range(0, 80):
    print(day)
    fishes.extend([9 for x in range(0, fishes.count(0))])
    fishes = [x - 1 if x > 0 else 6 if x == 0 else x for x in fishes]

print(len(fishes))