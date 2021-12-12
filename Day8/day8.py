def part1(input):
    sum = 0
    for digitInput in input:
        for digits in digitInput:
            if(1 < len(digits) and len(digits) < 5 or len(digits) == 7): sum +=1
    print("part1:", sum)

def commonCharacters(s1, s2):
    count = 0
    for carac in s1:
        if carac in s2: count += 1
    return count

def part2(input):
    total = 0
    for digitInput in input:
        digitInput[0].sort(key=len); left = digitInput[0]; right = digitInput[1]
        for i in range(len(left)): left[i] = "".join(sorted(left[i]))
        for i in range(len(right)): right[i] = "".join(sorted(right[i]))
        dictNumbers = {left[0]: 1, left[1]: 7, left[2]:4, left[9]:8}
        # we have to figure out which five and six digit belongs to
        fiveDigit = [left[3], left[4], left[5]]
        sixDigit = [left[6], left[7], left[8]]
        for i in range(len(sixDigit)):
            #6 is the only with 6 digits that has one common digit with 1
            if(commonCharacters(sixDigit[i], left[0]) == 1):
                dictNumbers[sixDigit[i]] = 6 
                del(sixDigit[i])
                break

        for i in range(len(sixDigit)):
            #9 is the only with 6 digits that has 4 common digits with 4
            if(commonCharacters(sixDigit[i], left[2]) == 4):
                dictNumbers[sixDigit[i]] = 9
                del(sixDigit[i])
                break
        
        #the only one left is the 0
        dictNumbers[sixDigit[0]] = 0
        
        for i in range(len(fiveDigit)):
            #3 is the only with 5 digits that has two common digits with 1
            if(commonCharacters(fiveDigit[i], left[0]) == 2):
                dictNumbers[fiveDigit[i]] = 3 
                del(fiveDigit[i])
                break

        for i in range(len(fiveDigit)):
            #2 is the only with 5 digits that has two common digits with 4
            if(commonCharacters(fiveDigit[i], left[2]) == 2):
                dictNumbers[fiveDigit[i]] = 2
                del(fiveDigit[i])
                break
    
        #the only one left is the 5
        dictNumbers[fiveDigit[0]] = 5

        #calculate total
        currTotal = 0
        for inputDigit in right:
            currTotal *=10
            currTotal += dictNumbers[inputDigit]
        total += currTotal
    print("part2:", total )
        

def main():
    f = open("input.txt", "r")
    input = f.readlines(); input1 = [i.strip().split('| ')[1].split(' ') for i in input]
    input2 = [i.strip().split(' | ')[k].split(' ') for i in input for k in range(0, 2)]
    input2 = [[input2[i], input2[i+1]] for i in range(0, int(len(input2)), 2)]
    part1(input1)
    part2(input2)
main()