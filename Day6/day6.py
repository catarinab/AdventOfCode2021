def solve(input, days, maxDays, resetTimer):
    fish = [0 for _ in range(maxDays+1)]
    for i in input: fish[i] +=1
    for _ in range(days):
        previous = fish[0]
        for i in range(maxDays):
            fish[i] = fish[i+1]
        fish[resetTimer] += previous
        fish[maxDays] = previous
    print(sum(fish))

def main():
    f = open("input.txt", "r")
    input = f.readlines(); input = list(map(int, input[0].split(',')));
    solve(input, 80, 8, 6)
    solve(input, 256, 8, 6)
main()