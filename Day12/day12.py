from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.V = 0
        self.initialVisitedDict = {}
        self.paths = 0
        self.smallCave = ""

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.initialVisitedDict[u] = (False)
        self.initialVisitedDict[v] = (False)

    def setVertices(self):
        self.V = len(self.initialVisitedDict)
    
    def chooseSmallCave(self):
        for i in self.graph:
            print(i, len(self.graph[i]))

    def printAllPaths(self, u, d, visited, path):
        if(u.islower() and u!= self.smallCave): visited[u]= True
        path.append(u)

        if u == d:
            self.paths +=1
            #print(path)
        else:
            for i in self.graph[u]:
                if visited[i]== False:
                    self.printAllPaths(i, d, visited, path)
                     
        path.pop()
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
    g.chooseSmallCave()
    g.printPaths("start", "end")
main()