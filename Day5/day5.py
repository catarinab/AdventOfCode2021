def main():
    f = open("input.txt", "r")
    lines = f.readlines(); points = []; pointsPassed =  [[[0]  for i in range(999)] for i in range(999)]
    for i in range(0, len(lines)): points.append(lines[i].strip().split(' ')); points[i].pop(1)
    for x in points:
        for i in range(0,2): x[i] = x[i].split(',')
        if(x[0][0] == x[1][0]): pass
        elif(x[0][1] == x[1][1]): pass
        else: continue

main()