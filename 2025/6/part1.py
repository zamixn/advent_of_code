

input_file = 'input.txt'
input_data = open(input_file).read()

lines = input_data.split('\n')

mathProblems = []

for p in lines[0].split():
    mathProblems.append([p])


for i in range(1, len(lines)):
    line = lines[i].split()
    for j, p in enumerate(line):
        mathProblems[j].append(p)

results = []

for p in mathProblems:
    operator = p[len(p) - 1]
    if(operator == "+"):
        result = 0
        for num in p[:-1]:
            result = result + int(num)
        results.append(result)
    elif(operator == "*"):
        result = 1
        for num in p[:-1]:
            result = result * int(num)
        results.append(result)

        
        
total = sum(results)
print(total)

