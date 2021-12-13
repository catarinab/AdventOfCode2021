from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.V = self.paths = 0
        self.initialVisitedDict = {}
        self.smallCaveName = ''

    def verifyStartEnd(self, u, i):
        return u != 'start' and i != 'start' and u != 'end' and i != 'end'

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.initialVisitedDict[u] = self.initialVisitedDict[v] = 0
        self.V +=1

    def printAllPaths(self, u, d, visited, path):
        if(u.islower()): visited[u] +=1
        path.append(u)

        if u == d: self.paths +=1
        else:
            for i in self.graph[u]:
                if visited[i] <= 0: self.printAllPaths(i, d, visited, path)
                elif visited[i] == 1 and i.islower() and self.smallCaveName == '' and self.verifyStartEnd(u, i):
                    self.smallCaveName = i
                    self.printAllPaths(i, d, visited, path)
    
        if(path.pop() == self.smallCaveName): self.smallCaveName = ''
        visited[u] -=1

    def printPaths(self, s, d):
        self.printAllPaths(s, d, self.initialVisitedDict, [])
        print(self.paths)

def main():
    input = open("input.txt", "r").readlines()
    for i in range(len(input)): input[i] = input[i].strip().split('-')
    g = Graph()
    for i in input: g.addEdge(i[0], i[1])
    g.printPaths("start", "end")
main()