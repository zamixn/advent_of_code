

input_file = 'input.txt'
input_data = open(input_file).read().split('\n\n')

rangesRaw = input_data[0].split("\n")
freshIdRanges = [(int(p.split("-")[0]), int(p.split("-")[1])) for p in rangesRaw]
ids = [int(id) for id in input_data[1].split("\n")]

print(freshIdRanges)

freshIdRangesProcessed = []
for r in freshIdRanges:
    s, e = r
    for rProcessed in freshIdRangesProcessed:
        sp, ep = rProcessed
        if(s >= sp and e <= ep):
            s = 0
            e = 0
            continue
        if(s < sp and e > ep):
            freshIdRangesProcessed.remove((sp, ep))
            continue
        if(s <= sp and e >= sp and e <= ep):
            e = sp - 1
            continue
        if(s >= sp and s <= ep and e >= ep):
            s = ep + 1
            continue
    
    if(s != 0 or e != 0):
        freshIdRangesProcessed.append((s, e))

print("\nprocessed")
print(freshIdRangesProcessed)


count = 0
for r in freshIdRangesProcessed:
    s, e = r
    count = count + (e - s) + 1

print(count) 

