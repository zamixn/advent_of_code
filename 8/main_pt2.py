fileLines = open("input.txt", 'r').readlines()
data = {x[0].rstrip():x[1].rstrip() for x in [x.split(" | ") for x in fileLines]}

def Remove(s1, s2):
    for c in s2:
        s1 = s1.replace(c, '')
    return s1

def Contains(s1, s2):
    for c in s2:
        if c not in s1:
            return False
    return True

sum = 0

for key in data:
    value = data[key]
    combos = value.split() + key.split()
    combos = ["".join(sorted(x)) for x in combos]
    outputs = ["".join(sorted(x)) for x in value.split()]
    signals = [''] * 10

    mappings = {
        'a': '',
        'b': '',
        'c': '',
        'd': '',
        'e': '',
        'f': '',
        'g': ''
    }

    for s in combos:
        if len(s) == 2:
            signals[1] = s
        elif len(s) == 4:
            signals[4] = s
        elif len(s) == 3:
            signals[7] = s
        elif len(s) == 7:
            signals[8] = s  

    mappings['a'] = Remove(signals[7], signals[1])

    #9, g
    for s in combos:
        charsToRemove = signals[4] + mappings['a']
        check = Remove(s, charsToRemove)
        if Contains(s, charsToRemove) and len(check) == 1:
            signals[9] = s
            mappings['g'] = check

    mappings['e'] = Remove(signals[8], signals[9])

    #3, d
    for s in combos:
        charsToRemove = mappings['a'] + mappings['g'] + signals[1]
        if Contains(s, charsToRemove) and len(Remove(s, charsToRemove)) == 1:
            signals[3] = s
            mappings['d'] = Remove(s, charsToRemove)

    #2, c
    for s in combos:
        charsToRemove = mappings['a'] + mappings['d'] + mappings['e'] + mappings['g']
        if Contains(s, charsToRemove) and len(Remove(s, charsToRemove)) == 1:
            signals[2] = s
            mappings['c'] = Remove(s, charsToRemove)

    mappings['f'] = Remove(signals[1], mappings['c'])
    mappings['b'] = Remove(signals[4], mappings['c'] + mappings['d'] + mappings['f'])

    signals[0] = Remove(signals[8], mappings['d'])
    signals[5] = Remove(signals[8], mappings['c'] + mappings['e'])
    signals[6] = Remove(signals[8], mappings['c'])

    signalToNum = {signals[x]:x for x in range(0, 10)}

    sum += int("".join([str(signalToNum[s]) for s in outputs]))

print(sum)