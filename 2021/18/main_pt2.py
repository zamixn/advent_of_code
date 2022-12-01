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
  AddToArray(posCopy, [velocity[0], velocity[1]])
  d1 = Distance(posCopy, targetAreaCenter)
  return pos[0] <= posCopy[0] or d1 < d0 or d1 < 100

def IsInArea(pos, area):
  return (pos[0] >= area[0][0] and pos[0] <= area[1][0] and
          pos[1] >= area[0][1] and pos[1] <= area[1][1])

velocities = [[x, y] for x in range(-200, 200) for y in range(-200, 200)]
maxYs = []
for velocity in velocities:
  vel = velocity.copy()
  pos = [0, 0]
  maxY = 0

  while CanStillReachTargetArea(pos, vel, targetAreaCenter) == True:
    AddToArray(pos, vel)
    AddToArray(vel, [-1, (-1 if vel[1] > 0 else (1 if vel[1] < 0 else 0))])

    if maxY < pos[0]:
      maxY = pos[0]

    if IsInArea(pos, targetArea):
      maxYs.append(velocity)
      break

print(len(maxYs))