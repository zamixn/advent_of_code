lines = open("input.txt", 'r').readlines()
draws = [int(s.rstrip()) for s in lines[0].split(',')]

boards = []
lineCount = 1
while lineCount < len(lines):
    board = [[int(num) for num in line.split()] for line in lines[(lineCount + 1):(lineCount + 6)]]
    lineCount += 6
    boards.append(board)

bingos = [[[False for x in range(5)] for y in range(5)] for x in range(len(boards))]

def IsWon(bingoBoard):
    b = False
    for y in range(5):
        for x in range(5):
            if bingoBoard[x][y] == False:
                b = True
                break
        if b == False:
            return True        
        b = False
    for x in range(5):
        for y in range(5):
            if bingoBoard[x][y] == False:
                b = True
                break
        if b == False:
            return True        
        b = False
    return False

def SumUnmarked(board, bingoBoard):
    sum = 0
    for x in range(5):
        for y in range(5):
            if bingoBoard[x][y] == False:
                sum += board[x][y]
    return sum

def Draw(draws, boards):
    boardsLeft = list(range(len(boards)))
    for draw in draws:
        for boardIndex, board in enumerate(boards):
            for x in range(5):
                for y in range(5):
                    if board[x][y] == draw:
                        bingos[boardIndex][x][y] = True
                        if(IsWon(bingos[boardIndex])):
                            if len(boardsLeft) == 1 and boardIndex in boardsLeft:
                                sum = SumUnmarked(board, bingos[boardIndex])
                                print ("sum: " + str(sum) + "; draw: " +str(draw))
                                return sum * draw
                            elif boardIndex in boardsLeft:
                                boardsLeft.remove(boardIndex)

print(Draw(draws, boards))