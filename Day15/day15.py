from collections import defaultdict
import heapq as heap

def validRange(vertice, lineSize):
    if(vertice%lineSize != 0 and vertice%lineSize != lineSize-1):
        return [vertice-1, vertice+1, vertice-lineSize, vertice+lineSize]
    elif(vertice%lineSize == 0):
        return [vertice+1, vertice-lineSize, vertice+lineSize]
    return [vertice-1, vertice-lineSize, vertice+lineSize]

def buildGraph(input):
    G = [{}]*(len(input)**2)
    for vertice in range(len(input)**2):
        G[vertice] = {}
        for item in validRange(vertice, len(input)):
            if(0 <= item < len(input)**2):
                G[vertice][item] = input[item//len(input)][item%len(input)]
    return G


def dijkstra(G, startingNode):
	visited = set()
	parentsMap = {}
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heap.heappush(pq, (0, startingNode))
 
	while pq:
		_, node = heap.heappop(pq)
		visited.add(node)
 
		for adjNode, weight in G[node].items():
			if adjNode in visited:	continue
				
			newCost = nodeCosts[node] + weight
			if nodeCosts[adjNode] > newCost:
				parentsMap[adjNode] = node
				nodeCosts[adjNode] = newCost
				heap.heappush(pq, (newCost, adjNode))
        
	return parentsMap, nodeCosts

def main():
    graph = open("input.txt", "r").readlines();
    for i in range(len(graph)): graph[i] = [int(item) for item in graph[i].strip()]
    print(dijkstra(buildGraph(graph), 0)[1][len(graph)**2-1]) #part1
main()

