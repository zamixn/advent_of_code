class number:
  def __init__(self):
    self.parent = None

class literal(number):
  def __init__(self, parent, value):
    self.value = value
    self.parent = parent

  def ToString(self, s = None):
    if s == None:
      s = ''
    
    s += str(self.value)
    return s

  def TryExplode(self):
    pass

class pair(number):
  def __init__(self, parent, left = None, right = None):
    self.left = left 
    self.right = right
    self.parent = parent

  def ToString(self, s = None):
    if s == None:
      s = ''
    
    left = self.left.ToString() if self.left != None else 'None'
    right = self.right.ToString() if self.right != None else 'None'
    s += '[' + left + ',' + right + ']'
    return s

  def ExplodeChild(self, isLeft):
    child = self.left if isLeft else self.right
    print("exploding: " + child.ToString())
    if isLeft  == True:
      self.left = literal(self, 0)
    else:
      self.right = literal(self, 0)

    


  def TryExplode(self):
    if (self.parent != None and self.parent.parent != None and
        self.parent.parent.parent != None and self.parent.parent.parent.parent != None):
        self.parent.ExplodeChild(self == self.parent.left)
        return True

    if self.left.TryExplode() == True:
      return True
    if self.right.TryExplode() == True:
      return True
    
    return False
    


def ReadLine(line):
  parts = [l.rstrip() for l in line[1:].split(',')]
  current = pair(None)
  head = current
  parsingRight = False
  for p in parts:
    openerCount = p.count('[')
    if openerCount > 0:
      for i in range(0, openerCount):
        child = pair(current)
        if parsingRight == False:
          current.left = child
        else:
          current.right = child
          parsingRight = False
        current = child
      current.left = literal(current, p[openerCount])
      parsingRight = True

    
    closerCount = p.count(']')
    if closerCount > 0:
      current.right = literal(current, p[0])
      for i in range(0, closerCount):
        current = current.parent
        parsingRight = True

    if openerCount == 0 and closerCount == 0:
      current.left = literal(current, p[0])
      parsingRight = True

  return head
  
def Add(base, additional):
  n = pair(None, base, additional)
  additional.parent = n
  base.parent = n
  return n

data = open("input_test2.txt", 'r').readlines()
num = ReadLine(data[0])
num.TryExplode()
for line in data[10:]:
  num = Add(num, ReadLine(line))
  num.TryExplode()
  print(num.ToString())

print(num.ToString())
