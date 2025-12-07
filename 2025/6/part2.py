

input_file = 'input.txt'
input_data = open(input_file).read()

lines = input_data.split('\n')
lineLen = len(lines[0])
operatorLine = lines[len(lines) - 1]
lines.pop(len(lines) - 1)

mathProblems = []

# seperate into colums-------------------------
def IsAllSpaces(columnIndex):
    for line in lines:
        if(line[columnIndex] != ' '):
            return False
    return True

problemSeperatorIndexes = []
for columnIndex in range(0, lineLen):
    if(IsAllSpaces(columnIndex)):
        problemSeperatorIndexes.append(columnIndex)
        continue
problemSeperatorIndexes.append(lineLen)

prevStart = 0
for seperatorIndex in problemSeperatorIndexes:
    numbers = []
    for line in lines:
        numbers.append(line[prevStart:seperatorIndex])
    mathProblems.append(numbers)
    prevStart = seperatorIndex + 1   

#print(problemSeperatorIndexes)
#print(mathProblems)
# -------------------------------------------
# parse into actual numbers -----------------
parsedMathProblems = []

for problem in mathProblems:
    parsedProblem = []
    for i in range(len(problem[0]) - 1, -1, -1):
        numberString = ""
        for p in problem:
            ch = p[i]
            if(ch == ' '):
                continue
            numberString = numberString + ch
        parsedProblem.append(int(numberString))
    parsedMathProblems.append(parsedProblem)
    
#print(parsedMathProblems)
# -------------------------------------------
# parse operators ---------------------------

operators = operatorLine.split()
# -------------------------------------------

results = []

for i, p in enumerate(parsedMathProblems):
    operator = operators[i]
    if(operator == "+"):
        result = 0
        for num in p:
            result = result + num
        results.append(result)
        #print(p, operator, result)
    elif(operator == "*"):
        result = 1
        for num in p:
            result = result * num
        results.append(result)
        #print(p, operator, result)

        
   
total = sum(results)
print(total)

