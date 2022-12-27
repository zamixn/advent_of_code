import re as regex

input_file = 'input_test.txt'

DEBUG = False

def PrintDebug(string):
    global DEBUG
    if DEBUG:
        print(string)
    

class Operator:
    def __init__(self, data):
        self.Data = data
        if data == '*':
            self.Evaluate = lambda l, r: l * r
        elif data == '+':
            self.Evaluate = lambda l, r: l + r
        else:
            print(f'Invalid operator data: {data}')
            exit(1)

    def __str__(self):
        return self.Data
    def __repr__(self):
        return str(self)

class Operand:
    def __init__(self, data):
        self.Data = data
        self.Old = -1
        if data != 'old':
            self.GetValue = lambda: int(data)
        else:
            self.GetValue = lambda: self.Old

    def __str__(self):
        return self.Data
    def __repr__(self):
        return str(self)

class Operation:
    def __init__(self, data):
        self.Data = data[data.index('=')+2:]
        parts = self.Data.split(' ')
        self.LeftOperand = Operand(parts[0])
        self.Operator = Operator(parts[1])
        self.RightOperand = Operand(parts[2])

    def Evaluate(self, oldValue):
        self.LeftOperand.Old = oldValue
        self.RightOperand.Old = oldValue
        return self.Operator.Evaluate(self.LeftOperand.GetValue(), self.RightOperand.GetValue())

    def __str__(self):
        return f'new = {self.LeftOperand}{self.Operator}{self.RightOperand}'
    def __repr__(self):
        return str(self)

class Test:
    def __init__(self, data):
        self.Condition = int(data[0][data[0].index('by')+3:])
        self.IfTrue = int(data[1][data[1].index('monkey')+7:])
        self.IfFalse = int(data[2][data[2].index('monkey')+7:])

    def GetThrowToIndex(self, worryLevel):
        if worryLevel % self.Condition == 0:
            return self.IfTrue
        else:
            return self.IfFalse

    def __str__(self):
        return f'divisible by: {self.Condition}, if true: {self.IfTrue}, if false: {self.IfFalse}'
    def __repr__(self):
        return str(self)


class Monkey:
    def __init__(self, data):
        lines = data.split('\n')
        self.Name = lines[0].strip('\n\t :')
        self.Items = [int(i) for i in regex.findall('\d.', lines[1])]
        self.Operation = Operation(lines[2])
        self.Test = Test(lines[3:])
        self.ItemInspectCount = 0

    def InspectItems(self):
        throwToPairList = []
        for i in range(0, len(self.Items)):
            worryLevel = self.Items[i]
            newWorryLevel = int(self.Operation.Evaluate(worryLevel) / 3)
            self.Items[i] = newWorryLevel
            throwToPairList.append((i, self.Test.GetThrowToIndex(newWorryLevel)))
            PrintDebug(f'{self.Name} inspecting: {i}, worryLevel: {worryLevel}; newWorryLevel: {newWorryLevel}')
            self.ItemInspectCount += 1
        return throwToPairList
        
    def ThrowItems(self, monkeys, throwToPairList):
        items = [i for i in self.Items]
        for pair in reversed(throwToPairList):
            PrintDebug(f'{self.Name} throwing: {self.Items[pair[0]]} to {monkeys[pair[1]].Name}')
            monkeys[pair[1]].AddItem(self.Items[pair[0]])
            del items[pair[0]]
        self.Items = items

    def AddItem(self, item):
        self.Items.append(item)

    def __str__(self):
        return f'Name: {self.Name}\nItems: {self.Items}\nOperation: {self.Operation}\nTest: {self.Test}\n'
    def __repr__(self):
        return str(self)


data = open(input_file).read().split('\n\n')
monkeys = [Monkey(d) for d in data]

rounds = 20
for i in range(0, rounds):
    for monkey in monkeys:
        throwToPairList = monkey.InspectItems()
        monkey.ThrowItems(monkeys, throwToPairList)

print([m.ItemInspectCount for m in monkeys])
monkeyBussiness = sorted([m.ItemInspectCount for m in monkeys], reverse=True)
monkeyBussiness = monkeyBussiness[0] * monkeyBussiness[1]
print(monkeyBussiness)