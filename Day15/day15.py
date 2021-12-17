from queue import PriorityQueue

def dist(x, y, xIndex, yIndex):
    return (((((x - xIndex )**2) + ((y-yIndex)**2) )**0.5) == 1)

def validRange(x, y, xIndex, yIndex, input):
    return (0 <= xIndex < len(input) and 0  <= yIndex < len(input[x]) and dist(x, y, xIndex, yIndex))

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    
    def add_edge(self, x, y, index, input):
        for xIndex in range(x-1, x+2):
            for yIndex in range(y-1, y+2):
                if(validRange(x, y, xIndex, yIndex, input)):
                    newIndex = len(input[0])*xIndex + yIndex
                    if(index > newIndex):
                        self.edges[newIndex][index] = input[x][y]

def dijkstra(graph, startVertex):
    print(graph.edges[16][15], graph.edges[15][16])
    D = {v:float('inf') for v in range(graph.v)}
    D[startVertex] = 0

    pq = PriorityQueue()
    pq.put((0, startVertex))

    while not pq.empty():
        (dist, currentVertex) = pq.get()
        graph.visited.append(currentVertex)
        print(currentVertex)

        for neighbor in range(graph.v):
            if graph.edges[currentVertex][neighbor] != -1:
                distance = graph.edges[currentVertex][neighbor]
                if neighbor not in graph.visited:
                    newCost = min(D[neighbor], D[currentVertex] + distance)
                    pq.put((newCost, neighbor))
                    if (currentVertex == 16): 
                        print(currentVertex, neighbor)
                    D[neighbor] = newCost
    return D

def main():
    input = open("inputtest.txt", "r").readlines()
    for i in range(len(input)): input[i] = [int(item) for item in input[i].strip()]
    g = Graph(len(input) * len(input[0]))
    for xIndex in range(len(input)):
        for yIndex in range(len(input[xIndex])): g.add_edge(xIndex, yIndex, len(input[0])*xIndex + yIndex, input)
    D = dijkstra(g, 0)
    print(D)
    #print(D[list(D.keys())[-1]])
main()

