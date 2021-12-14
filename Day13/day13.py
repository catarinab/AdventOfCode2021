def foldX(paper, x, maxY):
    paperSize = len(paper[0]) - 2
    for i in range(0, len(paper)): del paper[i][x]
    for i in range(0, x):
        for yIndex in range(0, maxY): 
            if(paper[yIndex][paperSize] == '#'): 
                paper[yIndex][i] = paper[yIndex][paperSize]
        for index in range(0, len(paper)): del paper[index][paperSize]
        paperSize -= 1

def foldY(paper, y, maxX):
    del paper[y]
    paperSize = len(paper) - 1
    for i in range(0, y):
        for xIndex in range(0, maxX + 2): 
            if(paper[paperSize][xIndex] == '#'): paper[i][xIndex] = paper[paperSize][xIndex]
        del paper[paperSize]
        paperSize -= 1

def part1(inputPaper, folds, paperMax):
    paper =  [['.'  for i in range(paperMax[0] + 1)] for i in range(paperMax[1]+ 1)]; hashtags = 0
    for i in inputPaper: paper[i[1]][i[0]] = '#'
    for fold in folds:
        if(fold[0] == 'y'): foldY(paper, fold[1], len(paper[0]) - 2)
        else: foldX(paper, fold[1], len(paper) - 1)
    for i in paper: print(' '.join(i).replace(".", " "))

def main():
    input = open("input.txt", "r").readlines(); inputPaper = []; folds = []; paperMax = (0, 0)
    for i in range(len(input)): 
        if(input[i][0] == '\n' ): break
        inputPaper.append(list(map(int,  input[i].strip().split(','))))
        paperMax = (max(inputPaper[i][0], paperMax[0]) , max(inputPaper[i][1], paperMax[1]))
    for k in range(i+1, len(input)): 
        result = input[k].strip().split(' ')[2].split('=')
        folds.append([result[0], int(result[1])])
    part1(inputPaper, folds, paperMax)
main()