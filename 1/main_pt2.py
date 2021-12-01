inputFile = "input.txt"

file1 = open(inputFile, 'r')
Lines = file1.readlines()

length = len(Lines)

increasedCount = 0
sums = []
for i in range(length - 2):
  line = Lines[i]
  
  sum = 0
  for j in range(i, i + 3):
    sum += int(Lines[j].rstrip())
  sums.append(sum)

  if i > 0:
    if sums[i] > sums[i-1]:
      increasedCount += 1
      print(str(sums[i]) + " increased")

  
  
print("\n\nAnswer:")
print(increasedCount)