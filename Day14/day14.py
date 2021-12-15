def part1(templateDict, pairs, steps):
    for step in range(steps):
        toAdd = {};  finalDict = {}
        for pair in templateDict:
            toAdd[pair] = templateDict[pair]
            templateDict[pair] = 0
        for item in toAdd:
            pairToAdd = pairs[item]
            for k in range(2):
                if(pairToAdd[k] in templateDict): templateDict[pairToAdd[k]] += toAdd[item]
                else: templateDict[pairToAdd[k]] = toAdd[item]
    finalDict[list(templateDict.keys())[0][0]] = templateDict[list(templateDict.keys())[0]]
    for pair in templateDict: 
        if(templateDict[pair] > 0):
            if(pair[1] in finalDict): finalDict[pair[1]] += templateDict[pair]
            else: finalDict[pair[1]] = templateDict[pair]
    print(finalDict[max(finalDict, key=finalDict.get)] - finalDict[min(finalDict, key=finalDict.get)])

def main():
    input = open("input.txt", "r").readlines(); pairs = {}; templateDict = {}
    template = input[0].strip()
    for i in range(2, len(input)):
        result = input[i].strip().split(' -> ')
        pairs[result[0]] = (result[0][0]+ result[1], result[1] + result[0][1])
    for i in range(0, len(template) - 1):
        if(template[i]+template[i+1] in templateDict): templateDict[template[i]+template[i+1]] += 1
        else: templateDict[template[i]+template[i+1]] = 1
    part1(templateDict, pairs, 40)
main()