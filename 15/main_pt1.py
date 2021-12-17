data = open("input.txt", 'r').readlines()
maze = [[int(i) for i in x.rstrip()] for x in data]

def printMatrix(matrix):
  print('\n'.join([''.join(['{:1}'.format(item) for item in row]) 
    for row in matrix]))

def printOpen(maze, openList):
  print('\n'.join([''.join(['{:1}'.format('+' if [y,x] in openList else '.') for x in range(0, len(maze[0]))]) 
    for y in range(0, len(maze))]))

def Backtrack(pos, maze, cameFrom):
  print(cameFrom) 
  path = [pos]
  while pos != [0, 0]:
    path.append(cameFrom[pos[0]][pos[1]])
    pos = cameFrom[pos[0]][pos[1]]
  return path[::-1]

def printPath(path, maze):
  print('\n'.join([''.join(['{:1}'.format('+' if [y,x] in path else '.') for x in range(0, len(maze[0]))]) 
    for y in range(0, len(maze))]))

maxY = len(maze)
maxX = len(maze[0])

print([maxY, maxX])

openList = []
closedList = []
cameFrom = [[[] for x in range(0, maxX)] for y in range(0, maxY)]
riskUpTo = [[999 for x in range(0, maxX)] for y in range(0, maxY)]
riskUpTo[0][0] = 0

openList.append([0, 0])

while len(openList) > 0:
  current = min(openList, key = lambda x: riskUpTo[x[0]][x[1]])

  if current == [maxY - 1, maxX - 1]:
    print("found path from [0, 0] to " + str(current))
    break

  openList.remove(current)
  closedList.append(current)

  currentRisk = riskUpTo[current[0]][current[1]]

  for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
    childIndex = [current[0] + i[0], current[1] + i[1]]

    if childIndex in closedList:
      continue

    if (childIndex[0] < 0 or childIndex[0] > maxY - 1 or
        childIndex[1] < 0 or childIndex[1] > maxX - 1):
      continue

    risk = currentRisk + maze[childIndex[0]][childIndex[1]]
    if riskUpTo[childIndex[0]][childIndex[1]] <= risk:
      continue

    openList.append(childIndex)
    cameFrom[childIndex[0]][childIndex[1]] = [current[0], current[1]]
    riskUpTo[childIndex[0]][childIndex[1]] = risk
  
  #printOpen(maze, openList)
  #print('\n\n')
        
#printMatrix(maze)

path = Backtrack([maxY - 1, maxX - 1], maze, cameFrom)
printPath(path, maze)
path.remove([0,0])
risk = riskUpTo[maxY - 1][maxX - 1]
print(risk)