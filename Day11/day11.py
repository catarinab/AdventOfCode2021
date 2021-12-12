def validRange(x, xIndex, yIndex, input):
    return (0 <= xIndex < len(input) and 0  <= yIndex < len(input[x])) and input [xIndex][yIndex] != 0

def flash(octupus, x, y):
    octupus[x][y] = 0
    for xIndex in range(x-1, x+2):
        for yIndex in range(y-1, y+2): 
            if(validRange(x, xIndex, yIndex, octupus)): octupus [xIndex][yIndex] =  octupus [xIndex][yIndex] + 1

def part2(octupus):
    flagFlash = 0; stepCounter = 0
    while(1):
        stepFlash = 0; stepCounter += 1
        for oct in octupus:
            for i in range(len(oct)): oct[i] = oct[i] + 1
        while(1):
            flagFlash = 0
            for xIndex in range(len(octupus)):
                for yIndex in range(len(octupus[xIndex])): 
                    if(octupus[xIndex][yIndex] > 9):
                        flash(octupus, xIndex, yIndex)
                        flagFlash = 1; stepFlash +=1
                if(flagFlash): break
            if(flagFlash == 0): break
        if(stepFlash == len(octupus) *len(oct)): 
            print(stepCounter)
            return
        
def main():
    f = open("input.txt", "r")
    input = f.readlines(); 
    for i in range(len(input)): input[i] = list(map(int, (char for char in input[i].strip())))
    part2(input)
main()