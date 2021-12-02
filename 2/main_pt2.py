inputFile = "input.txt"

file1 = open(inputFile, 'r')
Lines = file1.readlines()

xPos = 0
depth = 0
aim = 0

def do_forward(value):
    global xPos
    global depth
    global aim
    xPos += value
    depth += aim * value

def do_up(value):
    global aim
    aim -= value

def do_down(value):
    global aim
    aim += value

dispatch = {
    'forward': do_forward,
    'up': do_up,
    'down': do_down,
}

for line in Lines:
      parts = line.rstrip().split()
      dispatch[parts[0]](int(parts[1]))
  

print("\n\nValues: xPos:" + str(xPos) + "; depth: " + str(depth))
print("\nAnswer:")
print(xPos * depth)