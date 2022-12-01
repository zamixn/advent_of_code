paper = open("input.txt", 'r').read()
parts = paper.split('\n\n')
dots = [[int(x.split(',')[0]), int(x.split(',')[1])] for x in parts[0].split('\n')]
folds = [[x.split('=')[0].replace('fold along ', ''),int(x.split('=')[1])] for x in parts[1].split('\n')]

def Fold(dots, axis, foldLine):
    maxX = max(dots, key = lambda x: x[0])[0]
    maxY = max(dots, key = lambda x: x[1])[1]

    newDots = []
    if axis == 'y':
        for dot in dots:
            if dot[1] < foldLine:
                newdot = dot
            elif dot[1] > foldLine:
                newdot = [dot[0],foldLine - (dot[1] - foldLine)]

            if newdot not in newDots:
                newDots.append(newdot)
    else:
        for dot in dots:
            if dot[0] < foldLine:
                newdot = dot
            elif dot[0] > foldLine:
                newdot = [foldLine - (dot[0] - foldLine),dot[1]]
            
            if newdot not in newDots:
                newDots.append(newdot)

    return newDots


for fold in folds:
    dots = Fold(dots, fold[0], fold[1])
    break

print(len(dots))