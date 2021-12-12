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

    def solvePaths(self, u, d, visited, path): 
        if self.isBigCave(u) == False:
            visited[u] = True
        path.append(u)
 
        if u == d:
            self.paths.append(path.copy())
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.solvePaths(i, d, visited, path)                     
        path.pop()
        visited[u]= False
  
  
    def GetAllPaths(self, s, d):
        visited = {node:False for node in self.graph}
        path = [] 
        self.solvePaths(s, d, visited, path)
        return self.paths

fileLines = open("input.txt", 'r').readlines()
lines = [line.rstrip().split('-') for line in fileLines]

g = Graph()
for line in lines:
    g.addEdge(line[0], line[1])

paths = g.GetAllPaths('start', 'end')

print ('\n'.join([','.join(path) for path in paths]))
print("paths: " + str(len(paths)))