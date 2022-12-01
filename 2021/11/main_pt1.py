fileLines = open("input.txt", 'r').readlines()
octos = [[int(x) for x in line.rstrip()] for line in fileLines]

def PrintMatrix(matrix):
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in matrix]))

maxY = len(octos) - 1
maxX = len(octos[0]) - 1
flashesCount = 0
for step in range(0, 100):
    octos = [[x + 1 for x in o] for o in octos]

    flashed = [[0 for x in o] for o in octos]
    didFlash = True
    while didFlash == True:
        didFlash = False
        for y in range(0, maxY + 1):
            for x in range(0, maxX + 1):
                if octos[y][x] > 9 and flashed[y][x] == 0:
                    flashed[y][x] = 1
                    didFlash = True
                    
                    if x != maxX:
                        octos[y][x + 1] += 1
                    if x != 0:
                        octos[y][x - 1]  += 1
                    if y != maxY:
                        octos[y + 1][x] += 1
                    if y != 0:
                        octos[y - 1][x]  += 1
                    if x != maxX and y != 0:
                        octos[y - 1][x + 1] += 1
                    if x != maxX and y != maxY:
                        octos[y + 1][x + 1] += 1
                    if x != 0 and y != maxY:
                        octos[y + 1][x - 1] += 1
                    if x != 0 and y != 0:
                        octos[y - 1][x - 1] += 1
    
    for y in range(0, maxY + 1):
        for x in range(0, maxX + 1):
            if flashed[y][x] == 1:
                octos[y][x] = 0
                flashesCount += 1

    print("step: " + str(step + 1))
    PrintMatrix(octos)
    print()
    print()

print(flashesCount)