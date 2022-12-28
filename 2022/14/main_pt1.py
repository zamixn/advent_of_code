MOVING_SAND_SYMBOL = '+'
REST_SAND_SYMBOL = 'o'
ABBYSS_SAND_SYMBOL = '~'
EMPTY_SPACE_SYMBOL = '.'
ROCK_SYMBOL = '#'

class Point:
    def __init__(self, data):
        if isinstance(data, str):
            parts = data.split(',')
            parts = (int(parts[0]), int(parts[1]))
        else:
            parts = data
        self.X = parts[0]
        self.Y = parts[1]
    
    def __str__(self):
        return f'({self.X}, {self.Y})'
    def __repr__(self):
        return str(self)


class Line:
    def __init__(self, data):
        self.Start = Point(data[0])
        self.End = Point(data[1])
    
    def __str__(self):
        return f'{self.Start} -> {self.End}'
    def __repr__(self):
        return str(self)

class Sand:
    def __init__(self, spawnPoint):
        self.Pos = Point((spawnPoint.X, spawnPoint.Y))

class Terrain:
    def __init__(self, rockLines, sandSpawnPoint):
        self.RockLines = rockLines
        self.ActiveSandList = []
        self.SandSpawnPoint = sandSpawnPoint
        pMin = Point((sandSpawnPoint.X, sandSpawnPoint.Y))
        pMax = Point((sandSpawnPoint.X, sandSpawnPoint.Y))
        for rock in rockLines:
            for line in rock:
                pMin.X = min(pMin.X, line.Start.X, line.End.X)
                pMin.Y = min(pMin.Y, line.Start.Y, line.End.Y)
                pMax.X = max(pMax.X, line.Start.X, line.End.X)
                pMax.Y = max(pMax.Y, line.Start.Y, line.End.Y)
        self.MinPoint = pMin
        self.MaxPoint = pMax
        self.TerrainData = []

        for y in range(self.MinPoint.Y, self.MaxPoint.Y + 1):
            line = []
            for x in range(self.MinPoint.X, self.MaxPoint.X + 1):
                line.append(EMPTY_SPACE_SYMBOL)
            self.TerrainData.append(line)
        
        for rock in rockLines:
            for line in rock:
                for y in range(line.Start.Y, line.End.Y + 1):
                    for x in range(line.Start.X, line.End.X + 1):
                        self.AssignRock(x, y)
                for y in range(line.Start.Y, line.End.Y - 1, -1):
                    for x in range(line.Start.X, line.End.X - 1, -1):
                        self.AssignRock(x, y)


    def AssignRock(self, x, y):                        
        iy = self.PosToIndex(self.MinPoint.Y, y)
        ix = self.PosToIndex(self.MinPoint.X, x)
        self.TerrainData[iy][ix] = ROCK_SYMBOL


    def PosToIndex(self, start, pos):
        return pos - start

    def Print(self):
        lines = []
        for i in range(0, len(self.TerrainData)):
            line = []
            for j in range(0, len(self.TerrainData[i])):
                line.append(self.TerrainData[i][j])
            lines.append(line)

        for sand in self.ActiveSandList:
            iy = self.PosToIndex(self.MinPoint.Y, sand.Pos.Y)
            ix = self.PosToIndex(self.MinPoint.X, sand.Pos.X)
            lines[iy][ix] = MOVING_SAND_SYMBOL

        startPoint = self.MinPoint
        for i, line in enumerate(lines):
            strLine = ''.join(line)
            print(f'{startPoint.Y + i: <4}{strLine}')
                
    def TrySpawnSand(self):
        if len(self.ActiveSandList) > 0:
            return False
        self.ActiveSandList.append(Sand(self.SandSpawnPoint))
        return True

    def TryMoveSand(self):
        sandAtRest = []
        sandHasFallenToInfinity = False
        for sand in self.ActiveSandList:
            for i in range(0, 99999): # 99999 is a fail safe
                iy = self.PosToIndex(self.MinPoint.Y, sand.Pos.Y)
                ix = self.PosToIndex(self.MinPoint.X, sand.Pos.X)

                if sand.Pos.Y + 1 > self.MaxPoint.Y:
                    sandHasFallenToInfinity = True
                    break
                if self.TerrainData[iy + 1][ix] == EMPTY_SPACE_SYMBOL:
                    sand.Pos.Y += 1
                    continue

                if sand.Pos.X - 1 < self.MinPoint.X:
                    sandHasFallenToInfinity = True
                    break
                if self.TerrainData[iy + 1][ix - 1] == EMPTY_SPACE_SYMBOL:
                    sand.Pos.Y += 1
                    sand.Pos.X -= 1
                    continue

                
                if sand.Pos.X + 1 > self.MaxPoint.X:
                    sandHasFallenToInfinity = True
                    break
                if self.TerrainData[iy + 1][ix + 1] == EMPTY_SPACE_SYMBOL:
                    sand.Pos.Y += 1
                    sand.Pos.X += 1
                    continue
                # if we reach this point, sand can no longer move, assignIt to resting sand
                self.TerrainData[iy][ix] = REST_SAND_SYMBOL
                break;

            if sandHasFallenToInfinity:
                break
            sandAtRest.append(sand)

        if sandHasFallenToInfinity:
            return True
        
        for sand in sandAtRest:
            self.ActiveSandList.remove(sand)

        return False



input_file = 'input.txt'
input_data = open(input_file).read().split('\n')

rockLines = []
for line in input_data:
    parts = line.split(' -> ')
    rockLinesText = [(parts[i], parts[i+1]) for i in range(0, len(parts) - 1)]
    rockLines.append([Line(p) for p in rockLinesText])

sandSpawnPos = Point((500, 0))
terrain = Terrain(rockLines, sandSpawnPos)
print('== INITIAL STATE ==')
terrain.Print()

sandSpawned = 0
sandNotFallingToInfinity = True
while sandNotFallingToInfinity:
    terrain.TrySpawnSand()
    sandNotFallingToInfinity = not terrain.TryMoveSand()
    sandSpawned += 1    

print('\n== FINAL STATE ==')
terrain.Print()
print(f'SandAtRest: {sandSpawned - 1}') # -1 because the last sand spawned has fallen to the abbyss

