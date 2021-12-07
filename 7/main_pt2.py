fileLines = open("input.txt", 'r').readlines()
crabs = [int(x) for x in fileLines[0].split(',')]

def GetCost(p1, p2):
    n = abs(p1 - p2)
    return n / 2.0 * (2 + (n - 1))

def AlignTo(crabs, pos):
    fuel = sum([GetCost(x, pos) for x in crabs])
    return fuel

maxCrab = max(crabs)
fuelCosts = [AlignTo(crabs, x) for x in range(0, maxCrab)]
print(int(min(fuelCosts)))