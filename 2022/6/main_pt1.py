input_file = 'input.txt'

buffer = open(input_file).read()

sets_of_4 = [buffer[i-4:i] for i in range(4, len(buffer))]
marker = [i for i, elem in enumerate(sets_of_4) if len(set(elem)) == len(elem)][0] + 4

print(marker)