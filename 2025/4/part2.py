

input_file = 'input.txt'
input_data = open(input_file).read().split('\n')

paperMap = [list(line) for line in input_data]
N = 4
maxX = len(paperMap[0])
maxY = len(paperMap)

# debugMap = [list(line) for line in input_data]

def CanPickUp(x, y):
    n = 0

    # print("checking ", x, y)
    # print("x range: ", max(x - 1, 0), "->", min(x + 1, maxX))
    # print("y range: ", max(y - 1, 0), "->", min(y + 1, maxY))

    for nx in range(max(x - 1, 0), min(x + 2, maxX)):
        for ny in range(max(y - 1, 0), min(y + 2, maxY)):
            # print(nx, ny, "is", paperMap[ny][nx])
            if(nx == x and ny == y):
                continue
            if(paperMap[ny][nx] == "@"):
                n = n + 1
                if(n >= N):
                    return n
    return n


prevCount = -1
count = 0
while(True):
    prevCount = count

    for x in range(0, maxX):
        for y in range(0, maxY):
            if(paperMap[y][x] != "@"):
                continue


            n = CanPickUp(x, y)
            # debugMap[y][x] = str(n)
            if(n < N):
                count = count + 1
                paperMap[y][x] = "."

    if(prevCount == count):
        break;
        

print(count)

# print("\n")
# for row in debugMap:
#     print("".join(row))
