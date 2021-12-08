def result(x):
    return sum([int(x[i][k]) for k in range(0, 5) for i in range(0, len(x)) if x[i][k] != '*'])

def verify(x):
    for i in range(0, len(x)):
        if(x[i].count('*') == 5): return 1
    for i in range(0, 5): 
        if(x[0][i] == x[1][i] == x[2][i] == x[3][i] == x[4][i] == '*'): return 1
    return 0

def part1(lines):
    bingoNumbers = lines[0].strip().split(','); bingoNumber = 0; bingoCards = []
    for i in range(2, len(lines), 6): bingoCards.append([lines[i + k].strip().split(' ') for k in range(0,5)])
    for bingoNumber in range(0, len(bingoNumbers)): 
        for x in bingoCards:
            for i in range(0, len(x)):
                x[i] = ['*' if x[i][k] == bingoNumbers[bingoNumber] else x[i][k] for k in range(0, len(x[i]))]
            if(verify(x)): print(result(x)*int(bingoNumbers[bingoNumber])); return

def part2(lines):
    bingoNumbers = lines[0].strip().split(','); bingoNumber = 0; bingoCards = []; toRemove = []
    for i in range(2, len(lines), 6): bingoCards.append([lines[i + k].strip().split(' ') for k in range(0,5)])
    for bingoNumber in range(0, len(bingoNumbers)): 
        for x in bingoCards:
            for i in range(0, len(x)):
                x[i] = ['*' if x[i][k] == bingoNumbers[bingoNumber] else x[i][k] for k in range(0, len(x[i]))]
                if(verify(x)): toRemove.append(x); continue
        bingoCards = [x for x in bingoCards if x not in toRemove]
        if(len(bingoCards) == 0): print(result(x)*int(bingoNumbers[bingoNumber])); return

def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    part1(lines)
    part2(lines)
main()