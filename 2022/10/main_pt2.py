import math

input_file = 'input.txt'
XRegister = 1
Cycle = 0

ScreenX = 40
ScreenY = 6
ScreenBuffer = [['.'] * ScreenX for i in range(0, ScreenY)]
def PrintScreen():
    global ScreenY
    global ScreenBuffer
    for y in range(0, ScreenY):
        s = ''
        for x in range(0, ScreenX):
            s += ScreenBuffer[y][x]
        print(s)

def Render():
    global XRegister
    global Cycle
    global ScreenX
    global ScreenY
    global ScreenBuffer
    currRow = math.floor((Cycle - 1) / ScreenX)
    currPixel = (Cycle - 1)  % ScreenX
    if abs(XRegister - currPixel) <= 1:
        ScreenBuffer[currRow][currPixel] = '#'


def AddInstruction(value):
    global XRegister
    global Cycle
    NoOperationInstruction()
    Cycle += 1
    Render()
    XRegister += value

def NoOperationInstruction():
    global XRegister
    global Cycle
    Cycle += 1
    Render()

instructions = [i.split(' ') for i in open(input_file).read().split('\n')]

for i in instructions:
    if i[0] == 'noop':
        NoOperationInstruction()
    elif i[0] == 'addx':
        AddInstruction(int(i[1]))

PrintScreen()