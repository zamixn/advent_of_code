file1 = open("input.txt", 'r')
Lines = file1.readlines()
numbers = [int(numeric_string.rstrip(), 2) for numeric_string in Lines]
bit_len = len(Lines[0])

def GetProcessedBitAtIndex(numbers, bit_len, index, func):
    power = bit_len - (index + 1)
    mask = 1 << power
    bits = [int(((num & mask) << power) > 0 if 1 else 0) for num in numbers]
    return func(set(bits), key = bits.count)

gamma_str = ''
epsilon_str = ''
for i in range(bit_len):
    gamma_str += str(GetProcessedBitAtIndex(numbers, bit_len, i, max))
    epsilon_str += str(GetProcessedBitAtIndex(numbers, bit_len, i, min))

gamma = int(gamma_str, 2)
epsilon = int(epsilon_str, 2)
print(gamma * epsilon)