input_file = 'input.txt'

def GetChoice(input):
    return [input[0], chr((((ord(input[0]) - 64) + (ord(input[1]) - 89) - 1) % 3 + 1) + 87)]

def EvaluateRound(choices):
    opponent = ord(choices[0]) - 64
    player = ord(choices[1]) - 87
    won1 = (player > opponent and (player != 3 or opponent == 2)) or (player == 1 and opponent == 3)
    won2 = (player != opponent) != won1 
    return player + (won1 - won2 + 1) * 3

res = list(map(EvaluateRound, map(GetChoice, [x.split(' ') for x in open(input_file).read().split('\n')])))

print(sum(res))