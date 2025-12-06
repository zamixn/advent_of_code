

input_file = 'input.txt'
input_data = open(input_file).read()

def IsRepeatingPattern(pattern, s):

    end = len(s)
    stride = len(pattern)
    for i in range(0, end, stride):
        if(s[i:i+stride] != pattern):
            return False
    return True

def IsValid(num):
    s = str(num)
    i = 1
    end = int(len(s) / 2)
    for pattern_len in range(i, end + 1):
        if(IsRepeatingPattern(s[0:pattern_len], s) == True):
            return False
    return True

sum = 0
ranges = input_data.split(',')
for r in ranges:
    parts = r.split('-')
    start = int(parts[0])
    end = int(parts[1])

    for i in range(start, end + 1):
        if(IsValid(i) == False):
            sum = sum + i

print(sum)