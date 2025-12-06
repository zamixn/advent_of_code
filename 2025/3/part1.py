

input_file = 'input.txt'
input_data = open(input_file).read().split('\n')

joltage = 0
for line in input_data:
    lineLen = len(line)

    maxDigitIndex = 0
    maxDigit = 0
    for i, ch in enumerate(line[:-1]):
        num = int(ch)
        if(num > maxDigit):
            maxDigit = num
            maxDigitIndex = i
            print("maxDigit:", maxDigit, "index:", maxDigitIndex)
    
    secondMaxDigitIndex = 0
    secondMaxDigit = 0
    for i in range(maxDigitIndex + 1, lineLen):
        num = int(line[i])
        if(num > secondMaxDigit):
            secondMaxDigit = num
            print("secondMaxDigit:", secondMaxDigit, "index:", secondMaxDigitIndex)
            secondMaxDigitIndex = i

    s = str(maxDigit) + str(secondMaxDigit)
    print(line, s, "\n")

    joltage = joltage + int(s)

print(joltage)


