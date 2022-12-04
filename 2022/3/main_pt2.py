input_file = 'input.txt'

rucksacks = open(input_file).read().split('\n') # read file and get list of rucksacks
groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)] # group rucksacks into lists of 3
common = map(lambda parts : (set(parts[0]) & set(parts[1]) & set(parts[2])).pop(), groups) # get common parts of each group
priorities = map(lambda letter : ord(letter) - (96 if letter.islower() else 38), common) # convert common parts to their priorities

print(sum(priorities))