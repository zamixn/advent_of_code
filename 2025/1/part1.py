

input_file = 'input.txt'
input_data = open(input_file).read().split('\n')

dial = 50
count = 0

for line in input_data:
    direction = line[0]
    distance = int(line[1:])
    if(direction == 'L'):
        dial -= distance
        if(dial < 0):
            dial = (dial) % 100
    else:        
        dial += distance
        if(dial > 99):
            dial = dial % 100

    if(dial == 0):
        count = count + 1
    print(direction, " ", distance, " -> ", dial)

print(count)