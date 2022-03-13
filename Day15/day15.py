from collections import defaultdict
import heapq as heap
from copy import deepcopy
import itertools

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

def insertGraphRigth(expandedGraph, currentGraph, xGraphIndex, yGraphIndex, lineSize):
	for y, yIndex in zip(range(0, lineSize), range(yGraphIndex*lineSize, yGraphIndex*lineSize + lineSize)):
		for x, xIndex in zip(range(0, lineSize), range(xGraphIndex*lineSize, xGraphIndex*lineSize + lineSize)):
			expandedGraph[xIndex][yIndex] = currentGraph[x][y]

def defineExpandedGraph(size):
	expandedGraph = [[]]*(size *5)
	for i in range(size*5):
		expandedGraph[i] = []
		for _ in range(size*5):expandedGraph[i].append(0);
	return expandedGraph

def augmentGraph(currentGraph, size):
	for x,y in itertools.product(range(size), range(size)):
		if(currentGraph[x][y] < 9):
			currentGraph[x][y] = currentGraph[x][y] + 1
		else: currentGraph[x][y] = 1
	return currentGraph

def expandGraph(input):
	expandedGraph = defineExpandedGraph(len(input))
	previousGraph = deepcopy(input)
	currentGraph = deepcopy(input)
	for xIndex in range(5):
		previousGraph = deepcopy(currentGraph)
		for yIndex in range(5):
			insertGraphRigth(expandedGraph, currentGraph, xIndex, yIndex, len(input))
			currentGraph = augmentGraph(currentGraph, len(input))
		currentGraph = deepcopy(previousGraph)
		currentGraph = augmentGraph(currentGraph, len(input))
	return expandedGraph

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
	input = open("input.txt", "r").readlines();
	for i in range(len(input)): input[i] = [int(item) for item in input[i].strip()]
	print("part 1: ", dijkstra(buildGraph(input), 0)[1][len(input)**2-1])
	expandedGraph = expandGraph(input)
	print("part 2: ", dijkstra(buildGraph(expandedGraph), 0)[1][len(expandedGraph)**2-1])
main()

