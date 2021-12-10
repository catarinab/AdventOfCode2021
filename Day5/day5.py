def main():
    f = open("inputtest.txt", "r")
    lines = f.readlines(); points = []; pointsPassed =  [[[0]  for i in range(999)] for i in range(999)]; twoLines = 0
    for i in range(0, len(lines)): points.append(lines[i].strip().split(' ')); points[i].pop(1)
    for x in points:
        for i in range(0,2): x[i] = x[i].split(',')
        if(int(x[0][0]) > int(x[1][0])): x1 = int(x[1][0]); x2 = int(x[0][0])
        else: x1 = int(x[0][0]); x2 = int(x[1][0])
        if(int(x[0][1]) > int(x[1][1])): y1 = int(x[1][1]); y2 = int(x[0][1])
        else: y1 = int(x[0][1]); y2 = int(x[1][1])

        if(x[0][0] == x[1][0]):
            for k in range(y1, y2 + 1): pointsPassed[x1][k][0] += 1
        elif(x[0][1] == x[1][1]): 
            for k in range(x1, x2 + 1): pointsPassed[k][y1][0] += 1
        elif(x[0][0] == x[0][1] and x[1][0] == x[1][1]):
            for index in range(x1, x2+1): pointsPassed[index][index][0] += 1
        elif(x[0][0] == x[1][1] and x[0][1] == x[1][0]):
            for y_index in range(y1, y2 +1): 
                pointsPassed[x2][y_index][0] += 1
                x2 -=1

    for i in range(0, 10):
        for k in range(0,10):
            if(pointsPassed[i][k][0] >= 2): 
                twoLines +=1
                print(k, i, pointsPassed[i][k])
    print(twoLines)
"""
    for item in pointsPassed:
        for point in item:
            if(point[0] >= 2): 
                twoLines +=1
    print(twoLines)
    """

main()