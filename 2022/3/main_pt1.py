input_file = 'input.txt'

rucksacks = open(input_file).read().split('\n') # read file and get list of rucksacks
rucksack_parts = [ [r[0:int(len(r)/2)], r[int(len(r)/2):int(len(r))]] for r in rucksacks] # split each rucksack into two parts
common = map(lambda parts : (set(parts[0]) & set(parts[1])).pop(), rucksack_parts) # get common parts of each group
priorities = map(lambda letter : ord(letter) - (96 if letter.islower() else 38), common) # convert common parts to their priorities

print(sum(priorities))