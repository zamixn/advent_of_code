

input_file = 'input.txt'
input_data = open(input_file).read().split('\n')

N = 12

def GetLargestDigitIndex(startIndex, line, iteration):
    lineLen = len(line)
    maxDigitIndex = 0
    maxDigit = 0
    for i in range(startIndex, lineLen - (N - iteration - 1)):
        num = int(line[i])
        if(num > maxDigit):
            maxDigit = num
            maxDigitIndex = i
    return maxDigitIndex

joltage = 0
for line in input_data:

    digitIndexes = []
    prevIndex = -1;
    for i in range(0, N):
        prevIndex = GetLargestDigitIndex(prevIndex + 1, line, i)
        digitIndexes.append(prevIndex)    
    
    s = ""
    for idx in digitIndexes:
        s += line[idx]
    print(line, s, "\n")

    joltage = joltage + int(s)

print(joltage)


