def dist(x, y, xIndex, yIndex):
    return (((((x - xIndex )**2) + ((y-yIndex)**2) )**0.5) == 1)

def validRange(x, y, xIndex, yIndex, input):
    return (0 <= xIndex < len(input) and 0  <= yIndex < len(input[x]) and dist(x, y, xIndex, yIndex))

def lowLevel(input, x, y):
    result = 0; xStart = x-1; xEnd = x+2; yStart = y-1; yEnd = y+2;
    if(x == 0 or x == len(input) -1): result += 1
    if(y == 0 or y == len(input[x]) -1): result += 1
    for xIndex in range(xStart, xEnd):
        for yIndex in range(yStart, yEnd): 
            if(validRange(x, y, xIndex, yIndex, input)):
                if(input[x][y] < input[xIndex][yIndex]): result += 1
    return (result == 4)

def part1(input):
    riskLevel = 0; lowLevels = []
    for xIndex in range(len(input)):
        for yIndex in range(len(input[xIndex])):
            if(lowLevel(input, xIndex, yIndex)): 
                riskLevel +=1 + input[xIndex][yIndex]
                lowLevels.append((xIndex, yIndex))
    print(riskLevel)
    return lowLevels

def calcBasinSize(input, x, y, basinPoints, previousVal):
    xStart = x-1; xEnd = x+2; yStart = y-1; yEnd = y+2;
    for xIndex in range(xStart, xEnd):
        for yIndex in range(yStart, yEnd): 
            if(validRange(x, y, xIndex, yIndex, input) and previousVal < input[xIndex][yIndex] < 9):
                if((xIndex,yIndex) not in basinPoints): basinPoints.append((xIndex, yIndex))
                calcBasinSize(input, xIndex, yIndex, basinPoints, input[xIndex][yIndex])
    return len(basinPoints)

def part2(input, lowLevels):
    basins = [];
    for (xIndex, yIndex) in lowLevels:
            basins.append(calcBasinSize(input, xIndex, yIndex, [(xIndex, yIndex)], input[xIndex][yIndex]))
    basins.sort(reverse=True)
    print(basins[0]*basins[1]*basins[2])

def main():
    f = open("input.txt", "r")
    input = f.readlines(); 
    for i in range(len(input)): input[i] = list(map(int, (char for char in input[i].strip())))
    part2(input, part1(input))
main()