input_file = 'input.txt'

motions = [[line.split(' ')[0], int(line.split(' ')[1])] for line in open(input_file).read().split('\n')]

XMultiplierDics = {'R':1, 'L':-1, 'U':0, 'D':0}
YMultiplierDics = {'R':0, 'L':0, 'U':1, 'D':-1}

DEBUG = False

tailVisitedIndexes = []

def GetDistance(p1, p2):
    return Point(p2.X - p1.X, p2.Y - p1.Y)

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def toString(self):
        return f"({self.X}, {self.Y})"

class Tail(Point):
    def __init__(self, x, y):
        Point.__init__(self, x, y)
        self.VisitedIndexes = [(x, y)]
        self.Child = None

    def FollowParent(self, parent):
        d = GetDistance(self, parent)

        if abs(d.X) == 1 and abs(d.Y) > 1:
            self.X = parent.X
            d = GetDistance(self, parent)
        
        if abs(d.Y) == 1 and abs(d.X) > 1:
            self.Y = parent.Y
            d = GetDistance(self, parent)

        self.X += d.X - 1 if d.X > 1 else d.X + 1 if d.X < -1 else 0
        self.Y += d.Y - 1 if d.Y > 1 else d.Y + 1 if d.Y < -1 else 0

        currIndex = (self.X, self.Y)
        if not currIndex in self.VisitedIndexes:
            self.VisitedIndexes.append(currIndex)

        if self.Child != None:
            self.Child.FollowParent(self)


class Head(Point):
    def __init__(self, x, y, tailCount):
        Point.__init__(self, x, y)
        self.Tail = Tail(x, y)
        self.TailCount = tailCount;
        currTail = self.Tail
        for i in range(0, tailCount - 1):
            currTail.Child = Tail(x, y)
            currTail = currTail.Child

    def ApplyHeadMotion(self, motion):
        dX = XMultiplierDics[motion[0]]
        dY = YMultiplierDics[motion[0]]    

        PrintBoard(self, 6)
        for i in range(0, motion[1]):
            self.X += dX
            self.Y += dY
            self.Tail.FollowParent(self)           

            PrintBoard(self, 6)

    def GetLastTail(self):
        currTail = self.Tail
        for i in range(0, self.TailCount - 1):
            currTail = currTail.Child
        return currTail

def GetBoardSymbol(head, tailCount, posX, posY):
    s = '.'
    currTail = head.Tail
    tails = [currTail]
    for i in range(0, tailCount):
        currTail = currTail.Child
        tails.append(currTail)
    for i in range(tailCount - 1, -1, -1):        
        if posX == tails[i].X and posY == tails[i].Y:
            s = str(i + 1)

    s = 'H' if posX == head.X and posY == head.Y else s
    return s

def PrintBoard(head, size):
    if not DEBUG:
        return
    print()
    for y in range(size - 1, -1, -1):
        s = ''
        for x in range(0, size):
            s += GetBoardSymbol(head, head.TailCount, x, y)
        print(s)

head = Head(0, 0, 9)
print(f'\n======================== start ========================\n')
for motion in motions:
    if DEBUG:
        print(f'\n== {motion} ==')
    head.ApplyHeadMotion(motion)

print(len(head.GetLastTail().VisitedIndexes))

