input_file = 'input.txt'

def IsOverlapping(pair):
    return not (pair[0][1] < pair[1][0] or pair[0][0] > pair[1][1] )

pairs_raw = [x.split(',') for x in open(input_file).read().split('\n')]
pairs = [[[int(x) for x in p[0].split('-')], [int(x) for x in p[1].split('-')]] for p in pairs_raw]

overlapping = sum(map(IsOverlapping, pairs))
print(overlapping)