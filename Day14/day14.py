import collections
def part1(templateDict, pairs, steps):
    for step in range(steps):
        print(step)
        toAdd = {}; toDelete = []
        for pair in templateDict:
            toAdd[pair] = templateDict[pair]
            toDelete.append(pair)
        for item in toAdd:
            pairToAdd = pairs[item]
            for k in range(2):
                if(pairToAdd[k] in templateDict): templateDict[pairToAdd[k]] += toAdd[item]
                else: templateDict[pairToAdd[k]] = toAdd[item]
                if(pairToAdd[k] in toDelete): toDelete.remove(pairToAdd[k])
        print(templateDict)
        for item in toDelete:
            del templateDict[item]
        print(templateDict)
    result = list(templateDict.keys())[0][0]
    for pair in templateDict: 
        if(templateDict[pair] > 0):
            result += pair[1] * templateDict[pair]
    print(collections.Counter(result).most_common()[0][1] - collections.Counter(result).most_common()[-1][1])

def main():
    input = open("inputtest.txt", "r").readlines(); pairs = {}; templateDict = {}
    template = input[0].strip()
    for i in range(2, len(input)):
        result = input[i].strip().split(' -> ')
        pairs[result[0]] = (result[0][0]+ result[1], result[1] + result[0][1])
    for i in range(0, len(template) - 1):
        if(template[i]+template[i+1] in templateDict): templateDict[template[i]+template[i+1]] += 1
        else: templateDict[template[i]+template[i+1]] = 1
    part1(templateDict, pairs, 2)
main()