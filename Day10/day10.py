opening = ['(', '[', '{', '<']
closingDict = {')':'(', ']':'[', '}':'{', '>':'<'}
charsDict = {')':(0, 3), ']':(0, 57), '}':(0, 1197), '>':(0, 25137)}

def part1(input):
    openingChars = []; result = 0; toRemove = []
    for line in input:
        for char in line:
            if(char in opening): 
                openingChars.append(char)
            elif(closingDict[char] != openingChars.pop()):
                charsDict[char] = (charsDict[char][0] + 1, charsDict[char][1])
                toRemove.append(line)
    for item in toRemove: input.remove(item)
    for key in charsDict: result += charsDict[key][0]*charsDict[key][1]
    print(result)
    return input

def part2(input):
    results = []
    for line in input:
        openingChars = []
        for char in line:
            if(char in opening): 
                openingChars.append(char)
            else: openingChars.pop()
        result = 0
        openingChars.reverse()
        for item in openingChars:
            result *=5
            result += opening.index(item) + 1
        results.append(result)
    results.sort()
    print(results[int(len(results)/2)])

def main():
    f = open("input.txt", "r")
    input = f.readlines(); 
    for i in range(len(input)): input[i] = [char for char in input[i].strip()]
    part2(part1(input))
main()