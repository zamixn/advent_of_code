fileLines = open("input.txt", 'r').readlines()
crabs = [int(x) for x in fileLines[0].split(',')]

def AlignTo(crabs, pos):
    fuel = sum([abs(x - pos) for x in crabs])
    return fuel

maxCrab = max(crabs)
fuelCosts = [AlignTo(crabs, x) for x in range(0, maxCrab)]
print(min(fuelCosts))
