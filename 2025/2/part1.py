

input_file = 'input.txt'
input_data = open(input_file).read()

def IsRepeatingPattern(pattern, s):
    
    end = len(s)
    stride = len(pattern)
    for i in range(0, end, stride):
        if(s[i:i+stride] != pattern):
            print(s, pattern)
            return False
    
    print(s, pattern, "+")
    return True

def IsValid(num):
    s = str(num)
    mid = len(s) / 2
    if(mid != int(mid)):
        return True
    mid = int(mid)
    if(s[:mid] == s[mid:]):
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