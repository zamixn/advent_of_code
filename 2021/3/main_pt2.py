file1 = open("input.txt", 'r')
Lines = file1.readlines()
numbers = [int(numeric_string.rstrip(), 2) for numeric_string in Lines]
bit_len = len(Lines[0])    

def GetBitAtIndex(number, index):
    power = bit_len - (index + 1)
    mask = 1 << power
    return int(((number & mask) << power) > 0 if 1 else 0)

def GetProcessedBitAtIndex(numbers, bit_len, index, func):
    bits = [GetBitAtIndex(num, index) for num in numbers]
    return func(bits)

def GetProcessedNumber(numbers, bit_len, index, func):
    common = GetProcessedBitAtIndex(numbers, bit_len, index, func)
    sifted = list(filter(lambda x: GetBitAtIndex(x, index) == common, numbers))
    if(len(sifted) > 1):
        return GetProcessedNumber(sifted, bit_len, index + 1, func)
    else:
        return sifted[0]


c02 = GetProcessedNumber(numbers, bit_len, 1, lambda x: 1 if x.count(0) <= x.count(1) else 0)
oxygen = GetProcessedNumber(numbers, bit_len, 1, lambda x: 0 if x.count(0) <= x.count(1) else 1)

print("\nAnswer: " + str(c02 * oxygen))