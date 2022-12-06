input_file = 'input.txt'

raw_input = open(input_file).read().split('\n')
stacks_data_string = raw_input[:raw_input.index('') - 1]

stacks_data = list(reversed([list(stack[i:i+3] for i in range(0, len(stack), 4)) for stack in stacks_data_string]))
stacks = [[] for i in range(0, len(stacks_data[0])) ]

for stack in stacks_data:
    for i in range(0, len(stack)):
        if stack[i].strip(' ') != '':
            stacks[i].append(stack[i])

for command in raw_input[raw_input.index('')+1:]:
    parts = command.split(' ')
    count = int(parts[1])
    s1 = int(parts[3]) - 1
    s2 = int(parts[5]) - 1
    for i in range(0, count):
        stacks[s2].append(stacks[s1].pop())

top_most_crates = ''.join([(s[len(s) - 1]).strip('[]') for s in stacks])
print(top_most_crates)