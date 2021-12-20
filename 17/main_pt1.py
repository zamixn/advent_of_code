from math import dist
from os import replace

data = open("input.txt", 'r').readlines()[0].replace('target area:', '').replace(' ', '').split(',')
targetArea = [[int(s) for s in x.replace('x=', '').replace('y=', '').split('..')] for x in data]
targetArea = [[targetArea[1][0], targetArea[0][0]], [targetArea[1][1], targetArea[0][1]]]
targetAreaCenter = [(targetArea[1][0] + targetArea[0][0]) / 2.0, (targetArea[1][1] + targetArea[0][1]) / 2.0]
print(targetAreaCenter)

def AddToArray(array, arrayToAdd):
  array[0] += arrayToAdd[0]
  array[1] += arrayToAdd[1]

def Distance(pos1, pos2):
  return ((((pos2[1] - pos1[1] )**2) + ((pos2[0] - pos1[0])**2) )**0.5)

def CanStillReachTargetArea(pos, velocity, targetAreaCenter):
  d0 = Distance(pos, targetAreaCenter)
  posCopy = pos.copy()
  AddToArray(posCopy, velocity)
  d1 = Distance(posCopy, targetAreaCenter)
  #print(d0)
  #print(d1)
  return pos[0] <= posCopy[0] or d1 < d0

def IsInArea(pos, area):
  return (pos[0] >= area[0][0] and pos[0] <= area[1][0] and
          pos[1] >= area[0][1] and pos[1] <= area[1][1])

velocities = [[x, y] for x in range(-100, 100) for y in range(-100, 100)]
maxYs = {}
for velocity in velocities:
  pos = [0, 0]
  maxY = 0

  while CanStillReachTargetArea(pos, velocity, targetAreaCenter) == True:
    AddToArray(pos, velocity)
    AddToArray(velocity, [-1, (-1 if velocity[1] > 0 else (1 if velocity[1] < 0 else 0))])
    #print(pos)
    #print(velocity)
    #print('\n\n')

    if maxY < pos[0]:
      maxY = pos[0]

    if IsInArea(pos, targetArea):
      #print("target reached; maxY: " + str(maxY))
      maxYs[maxY] = velocity
      break

print(max(maxYs.keys()))

