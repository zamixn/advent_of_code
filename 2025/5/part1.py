

input_file = 'input.txt'
input_data = open(input_file).read().split('\n\n')

rangesRaw = input_data[0].split("\n")
freshIdRanges = [(int(p.split("-")[0]), int(p.split("-")[1])) for p in rangesRaw]
ids = [int(id) for id in input_data[1].split("\n")]

def IsInRange(r, id):
    s, e = r
    return id >= s and id <= e

print(freshIdRanges)
print(ids)

count = 0
for id in ids:
    for r in freshIdRanges:
        if(IsInRange(r, id)):
            count = count + 1
            break;

print(count) 

