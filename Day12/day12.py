from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.V = 0
        self.initialVisitedDict = {}
        self.paths = 0
        self.secSmallCave = False
        self.smallCaveName = ''''''

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.initialVisitedDict[u] = (False)
        self.initialVisitedDict[v] = (False)

    def setVertices(self):
        self.V = len(self.initialVisitedDict)

    def printAllPaths(self, u, d, visited, path):
        if(u.islower()):
            visited[u]= True
        path.append(u)

        if u == d:
            self.paths +=1
        else:
            for i in self.graph[u]:
                print(u, i)
                if visited[i]== False:
                    print("Nao visitado")
                    print(path)
                    self.printAllPaths(i, d, visited, path)
                elif self.secSmallCave == False and i.islower() and u != 'start' and i != 'start' and u != 'end' and i != 'end':
                    self.secSmallCave = True
                    self.smallCaveName = i
                    print("Nao visitado")
                    print(path)
                    self.printAllPaths(i, d, visited, path)
                 
        cave = path.pop()
        if(cave == self.smallCaveName):
            print(cave, self.smallCaveName, "self.secSmallCave = False")
            self.secSmallCave = ''''''
            self.secSmallCave = False
        visited[u]= False

    def printPaths(self, s, d):
        self.printAllPaths(s, d, self.initialVisitedDict, [])
        print(self.paths)

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