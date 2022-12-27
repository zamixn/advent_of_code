import re as regex

input_file = 'input.txt'

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

    def EvaluateConstant(self, leftConstant):
        return self.Operator.Evaluate(leftConstant, self.RightOperand.GetValue())

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

class Item:
    def __init__(self, value):
        self.Value = value
        self.RemainderDict = {}

    def SetDivisors(self, devisors):
        for d in devisors:
            self.RemainderDict[d] = self.Value % d

    def SetValue(self, operation):
        for key in self.RemainderDict.keys():            
            newVal = operation.Evaluate(self.RemainderDict[key])
            self.RemainderDict[key] = newVal % key

    def GetValue(self, devisor):
        return self.RemainderDict[devisor]

    def __str__(self):
        return f'{self.Value}'
    def __repr__(self):
        return str(self)

class Monkey:
    def __init__(self, data):
        lines = data.split('\n')
        self.Name = lines[0].strip('\n\t :')
        self.Items = [Item(int(i)) for i in regex.findall('\d.', lines[1])]
        self.Operation = Operation(lines[2])
        self.Test = Test(lines[3:])
        self.ItemInspectCount = 0

    def InspectItems(self):
        throwToPairList = []
        for i in range(0, len(self.Items)):
            self.Items[i].SetValue(self.Operation)
            newWorryLevel = self.Items[i].GetValue(self.Test.Condition)
            throwToPairList.append((i, self.Test.GetThrowToIndex(newWorryLevel)))
            PrintDebug(f'{self.Name} inspecting: {i}')
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
devisors = [m.Test.Condition for m in monkeys]
for m in monkeys:
    for i in m.Items:
        i.SetDivisors(devisors)

rounds = 10000
for i in range(1, rounds + 1):
    for monkey in monkeys:
        throwToPairList = monkey.InspectItems()
        monkey.ThrowItems(monkeys, throwToPairList)


monkeyBussiness = sorted([m.ItemInspectCount for m in monkeys], reverse=True)
print(monkeyBussiness)
monkeyBussiness = monkeyBussiness[0] * monkeyBussiness[1]
print(monkeyBussiness)

