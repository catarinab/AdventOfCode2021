from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.V = 0
        self.initialVisitedDict = {}

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.initialVisitedDict[u] = (False)
        self.initialVisitedDict[v] = (False)

    def setVertices(self):
        self.V = len(self.initialVisitedDict)
        print(self.graph)

    def printAllPaths(self, u, d, visited, path):
        visited[u]= True
        path.append(u)

        if u == d:
            print(path)
        else:
            for i in self.graph[u]:
                if visited[i]== False:
                    self.printAllPaths(i, d, visited, path)
                     
        path.pop()
        visited[u]= False

    def printPaths(self, s, d):
        self.printAllPaths(s, d, self.initialVisitedDict, [])

def main():
    f = open("inputtest.txt", "r")
    input = f.readlines(); 
    for i in range(len(input)): input[i] = input[i].strip().split('-')
    g = Graph()
    for i in input:
        g.addEdge(i[0], i[1])
        g.addEdge(i[1], i[0])
    g.setVertices()
    g.printPaths("start", "end")
main()