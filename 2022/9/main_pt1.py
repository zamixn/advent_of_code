input_file = 'input.txt'

motions = [[line.split(' ')[0], int(line.split(' ')[1])] for line in open(input_file).read().split('\n')]

XMultiplierDics = {'R':1, 'L':-1, 'U':0, 'D':0}
YMultiplierDics = {'R':0, 'L':0, 'U':1, 'D':-1}


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

    def FollowHead(self, head):
        d = GetDistance(self, head)

        if abs(d.X) == 1 and abs(d.Y) > 1:
            self.X = head.X
            d = GetDistance(self, head)
        
        if abs(d.Y) == 1 and abs(d.X) > 1:
            self.Y = head.Y
            d = GetDistance(self, head)

        self.X += d.X - 1 if d.X > 1 else d.X + 1 if d.X < -1 else 0
        self.Y += d.Y - 1 if d.Y > 1 else d.Y + 1 if d.Y < -1 else 0

        currIndex = (self.X, self.Y)
        if not currIndex in self.VisitedIndexes:
            self.VisitedIndexes.append(currIndex)


class Head(Point):
    def __init__(self, x, y):
        Point.__init__(self, x, y)
        self.Tail = Tail(x, y)

    def ApplyHeadMotion(self, motion):
        dX = XMultiplierDics[motion[0]]
        dY = YMultiplierDics[motion[0]]    

       # PrintBoard(self, self.Tail, 6)
        for i in range(0, motion[1]):
            self.X += dX
            self.Y += dY
            self.Tail.FollowHead(self)           

            #PrintBoard(self, self.Tail, 6)

def PrintBoard(head, tail, size):
    print()
    for y in range(size - 1, -1, -1):
        s = ''
        for x in range(0, size):
            s += 'H' if head.X == x and head.Y == y else 'T' if tail.X == x and tail.Y == y else '.'
        print(s)

head = Head(0, 0)
print(f'\n======================== start ========================\n')
for motion in motions:
    #print(f'\n== {motion} ==')
    head.ApplyHeadMotion(motion)

print(len(head.Tail.VisitedIndexes))

