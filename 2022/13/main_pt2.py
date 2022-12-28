DEBUG = False
def PrintWithIndent(string, indentCount):
    global DEBUG
    if not DEBUG:
        return
    indent = '  ' * indentCount
    print(f'{indent}{string}')

class Packet:
    def __init__(self, data, startSkipIndex = 1):
        self.Data = []
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
    
    def __cmp__(self, other):
        return self.Compare(other, 0)

    def __lt__(self, obj):
        return self.Compare(obj) < 0
  
    def __gt__(self, obj):
        return self.Compare(obj) > 0
  
    def __le__(self, obj):
        return self.Compare(obj) <= 0
  
    def __ge__(self, obj):
        return self.Compare(obj) <= 0
  
    def __eq__(self, obj):
        return self.Compare(obj) == 0

input_file = 'input.txt'
packets = [Packet(d) for d in open(input_file).read().split('\n') if d]

firstDivider = Packet('[[2]]')
secondDivider = Packet('[[6]]') 
packets.append(firstDivider)
packets.append(secondDivider)

packets.sort()
print(packets)

i = packets.index(firstDivider) + 1
j = packets.index(secondDivider) + 1
print(i * j)


