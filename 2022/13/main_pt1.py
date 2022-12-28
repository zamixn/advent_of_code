DEBUG = True
def PrintWithIndent(string, indentCount):
    global DEBUG
    if not DEBUG:
        return
    indent = '  ' * indentCount
    print(f'{indent}{string}')

class Packet:
    def __init__(self, data, startSkipIndex = 1):
        self.Data = []
        print(data)
        rawData = eval(data)
        if isinstance(rawData, int):
            self.Data.append(rawData)
        else:
            for d in rawData:
                if isinstance(d, int):
                    self.Data.append(d)
                else:
                    self.Data.append(str(d).strip().replace(' ', ''))

    def __str__(self):
        return f'{self.Data}'
    def __repr__(self):
        return str(self)

    def Compare(self, other, indent = 0):
        PrintWithIndent(f'- Compare {self} vs {other}', indent)
        indent += 1
        for i, lvalue in enumerate(self.Data):
            if i > len(other.Data) - 1:
                PrintWithIndent(f'- right side ran out of items, input INCORRECT', indent)
                return 1

            rvalue = other.Data[i]

            if isinstance(rvalue, int) and isinstance(lvalue, int):    
                PrintWithIndent(f'- Compare {lvalue} vs {rvalue}', indent)    
                if lvalue == rvalue:
                    continue
                if lvalue < rvalue:
                    PrintWithIndent(f'- Left side is smaller, inputs CORRECT', indent + 1)    
                    return -1
                if lvalue > rvalue:
                    PrintWithIndent(f'- Right side is smaller, inputs INCORRECT', indent + 1)    
                    return 1

            lvaluePacket = lvalue 
            if not isinstance(lvalue, Packet):
                PrintWithIndent(f'- converting left: {lvalue}', indent + 1)
                lvaluePacket = Packet(f'{lvalue}', startSkipIndex = 0)            
            rvaluePacket = rvalue 
            if not isinstance(rvalue, Packet):
                PrintWithIndent(f'- converting right: {rvalue}', indent + 1)
                rvaluePacket = Packet(f'{rvalue}', startSkipIndex = 0)

            compResult = lvaluePacket.Compare(rvaluePacket, indent=indent + 1)
            if compResult == 0:
                continue

            #print(f'converted, compared {lvaluePacket} with {rvaluePacket}. False')
            return compResult
        
        if len(self.Data) < len(other.Data):
            PrintWithIndent(f'- left side ran out of items, input CORRECT', indent)
            return -1
        elif len(self.Data) > len(other.Data):
            PrintWithIndent(f'- right side ran out of items, input INCORRECT', indent)
            return 1

        return 0

class Pair:
    def __init__(self, data, index):
        packets = data.split('\n')
        self.LeftPacket = Packet(packets[0])
        self.RightPacket = Packet(packets[1])
        self.Index = index + 1

    def __str__(self):
        return f'{self.Index}\n {self.LeftPacket}\n {self.RightPacket}\n Is in right order: {self.IsInRightOrder()}'
    def __repr__(self):
        return str(self)

    def IsInRightOrder(self):
        return self.LeftPacket.Compare(self.RightPacket) < 0

input_file = 'input.txt'
packetPairs = [Pair(d, i) for i, d in enumerate(open(input_file).read().split('\n\n'))]

correctPairIndexes = [p.Index for p in packetPairs if p.IsInRightOrder()]
print(sum(correctPairIndexes))
print(correctPairIndexes)