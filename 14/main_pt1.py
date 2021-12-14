data = open("input.txt", 'r').readlines()
template = data[0].rstrip()
pairs = [data[x].rstrip() for x in range(2, len(data))]
pairs = {p.split(' -> ')[0]:p.split(' -> ')[1] for p in pairs}

for i in range(0, 10):
    newTemplate = template

    for pairIndex in range(len(template), 0, -1):
        pair = template[pairIndex - 2: pairIndex: 1]
        if pair in pairs:
            newTemplate = newTemplate[:pairIndex - 1] + pairs[pair] + newTemplate[pairIndex - 1:]

    template = newTemplate 
    print(template)
    print()

histogram = {x:template.count(x) for x in set(template)}
histogram = list(dict(sorted(histogram.items(), key = lambda x: x[1])).values())
print(histogram[-1] - histogram[0])