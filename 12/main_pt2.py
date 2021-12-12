from collections import defaultdict

class Graph:  
    def __init__(self):
        self.graph = defaultdict(list)
        self.paths = []
  
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
  
    def isBigCave(self, u):
        return u.isupper()

    def solvePaths(self, u, d, visited, path, smallCaveDoubled):
        visited[u] += 1
        path.append(u)
 
        if u == d:
            self.paths.append(path.copy())
        else:
            for i in self.graph[u]:
                if self.isBigCave(i) == True or visited[i] == 0:
                    self.solvePaths(i, d, visited, path, smallCaveDoubled)
                elif visited[i] == 1 and i != 'start' and i != 'end':                    
                    if i == smallCaveDoubled or smallCaveDoubled == '':
                        self.solvePaths(i, d, visited, path, i)                     
        path.pop()
        visited[u] -= 1
  
    def GetAllPaths(self, s, d):
        visited = {node:0 for node in self.graph}
        path = [] 
        self.solvePaths(s, d, visited, path, '')
        return self.paths

fileLines = open("input.txt", 'r').readlines()
lines = [line.rstrip().split('-') for line in fileLines]

g = Graph()
for line in lines:
    g.addEdge(line[0], line[1])

paths = g.GetAllPaths('start', 'end')

print ('\n'.join([','.join(path) for path in paths]))
print("paths: " + str(len(paths)))