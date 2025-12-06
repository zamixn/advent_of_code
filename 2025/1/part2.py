

input_file = 'input.txt'
input_data = open(input_file).read().split('\n')

pointer = 50
counter = 0
N = 100

for line in input_data:
    delta = int(line[1:])
    if line[0] == "L":
        delta = -delta
    dist = (N - pointer) if delta > 0 else pointer or N
    if abs(delta) >= dist:
        counter += 1 + (abs(delta) - dist) // N
    pointer = (pointer + delta) % N

print(counter)