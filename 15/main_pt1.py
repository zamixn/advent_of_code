data = open("input_test.txt", 'r').readlines()
maze = [[int(i) for i in x.rstrip()] for x in data]

def printMatrix(matrix):
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) 
      for row in matrix]))

maxY = len(maze)
maxX = len(maze[0])

openList = []
closedList = []

openList.append([0, 0])

while len(openList) > 0:
  current = min(openList, key = lambda x: maze[x[0]][x[1]])
  openList.remove(current)
  closedList.append(current)

  if current == [maxY - 1, maxX - 1]:
    print("found path")
    break

  for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
    childIndex = [current[0] + i[0], current[1] + i[1]]

    if childIndex in closedList:
      continue

    if (childIndex[0] < 0 or childIndex[0] > maxY - 1 or
        childIndex[1] < 0 or childIndex[1] > maxX - 1):
        continue

    #if maze[childIndex[0]][childIndex[1]] >


    openList.append(childIndex)
        
#printMatrix(maze)

risk = sum([maze[i[0]][i[1]] for i in openList])
print(risk)