input_file = 'input.txt'

buffer = open(input_file).read()

sets_of_14 = [buffer[i-14:i] for i in range(14, len(buffer))]
marker = [i for i, elem in enumerate(sets_of_14) if len(set(elem)) == len(elem)][0] + 14

print(marker)