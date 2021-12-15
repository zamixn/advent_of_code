data = open("input_test.txt", 'r').readlines()
maze = [[int(i) for i in x.rstrip()] for x in data]

def printMatrix(matrix):
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) 
      for row in matrix]))

printMatrix(maze)