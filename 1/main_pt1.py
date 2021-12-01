inputFile = "input.txt"

file1 = open(inputFile, 'r')
Lines = file1.readlines()

increasedCount = 0
prevI = -1
for line in Lines:
  i = line.rstrip()
  if prevI == -1:
    prevI = i
  
  if i >= prevI:
    increasedCount += 1
    print(str(i) + " increased")
  else:
    print(i)
  
  prevI = i
  
print("\n\nAnswer:")
print(increasedCount)