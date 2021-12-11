def calculateScore(currentIndex, crabs):
    score = 0
    for i in range(0, len(crabs)):
        arithmeticSum = (abs(i-currentIndex)*(abs(i-currentIndex) +1))/2 #arithmetic sum
        score += arithmeticSum*crabs[i]
    return score

def solve(input, maxInput):
    crabs = [0 for _ in range(maxInput)] 
    for i in input: crabs[i] +=1
    minScore = calculateScore(0, crabs)
    for crabsIndex in range(1, maxInput):
        currentScore = calculateScore(crabsIndex, crabs)
        if(currentScore < minScore): 
            minScore = currentScore
    print(minScore)

def main():
    f = open("input.txt", "r")
    input = f.readlines(); input = list(map(int, input[0].split(',')));
    solve(input, max(input) + 1)
main()