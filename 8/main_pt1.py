fileLines = open("input.txt", 'r').readlines()
data = {x[0].rstrip():x[1].rstrip() for x in [x.split(" | ") for x in fileLines]}

counts = [0] * 10

for key in data:
    value = data[key]
    outputs = value.split()
    signals = {x:[] for x in range(0, 10)}
    tempCounts = [0] * 10

    for s in outputs:
        if len(s) == 2 and s not in signals[1]:
            signals[1].append(s)
        elif len(s) == 4 and s not in signals[4]:
            signals[4].append(s)
        elif len(s) == 3 and s not in signals[7]:
            signals[7].append(s)
        elif len(s) == 7 and s not in signals[8]:
            signals[8].append(s)

            

    for i in range(0, 10):
        for signal in signals[i]:
            tempCounts[i] += outputs.count(signal)
        
    for i in range(0, 10):
        counts[i] += tempCounts[i]

print(sum(counts))