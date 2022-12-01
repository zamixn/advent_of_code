from itertools import groupby

input_file = 'input.txt'

lines = [int(x) if x.isdecimal() else '' for x in open(input_file).read().split('\n')]
grouper = groupby(lines, key = lambda x : x == '')
split = list(dict(enumerate((list(j) for i, j in grouper if not i), 1)).values())
res = sum(sorted([sum(x) for x in split])[len(split) - 3 : len(split)])

print(res)