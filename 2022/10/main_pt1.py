input_file = 'input.txt'
XRegister = 1
Cycle = 0
CycleDict = {}

def SaveCycle():
    global XRegister
    global Cycle
    global CycleDict
    CycleDict[Cycle] = XRegister


def AddInstruction(value):
    global XRegister
    global Cycle
    NoOperationInstruction()
    Cycle += 1
    SaveCycle()
    XRegister += value

def NoOperationInstruction():
    global XRegister
    global Cycle
    Cycle += 1
    SaveCycle()

instructions = [i.split(' ') for i in open(input_file).read().split('\n')]

for i in instructions:
    if i[0] == 'noop':
        NoOperationInstruction()
    elif i[0] == 'addx':
        AddInstruction(int(i[1]))


start = 20
step = 40
importantCycles = {}
for i in range(start, 9999999, step):
    if(i not in CycleDict):
        break
    importantCycles[i] = CycleDict[i]

s = 0
for i in importantCycles:
    s += i * importantCycles[i]

print(s)

# print(XRegister, Cycle, '\n', importantCycles)

# print('\n\n\n', CycleDict)