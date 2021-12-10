def declive(x1, x2, y1, y2):
    return (y1-y2)/(x1-x2)

def definexy(x00,x01,y10,y11):
    if(x00 > x01): x1 = x01; x2 = x00
    else: x1 = x00; x2 = x01
    if(y10 > y11): y1 = y11; y2 = y10
    else: y1 = y10; y2 = y11
    return x1,x2,y1,y2
    
def main():
    f = open("input.txt", "r")
    lines = f.readlines(); points = []; pointsPassed =  [[[0]  for i in range(999)] for i in range(999)]; twoLines = 0
    for i in range(0, len(lines)): points.append(lines[i].strip().split(' ')); points[i].pop(1)
    for x in points:
        for i in range(0,2): x[i] = x[i].split(',')
        x1,x2,y1,y2 = definexy(int(x[0][0]), int(x[1][0]), int(x[0][1]), int(x[1][1]))

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
        elif(declive(int(x[0][0]), int(x[1][0]), int(x[0][1]), int(x[1][1])) == -1):
            for y_index in range(y1, y2 +1): 
                pointsPassed[x2][y_index][0] += 1
                x2 -=1
        elif(declive(int(x[0][0]), int(x[1][0]), int(x[0][1]), int(x[1][1])) == 1):
            for y_index in range(y1, y2 +1): 
                pointsPassed[x1][y_index][0] += 1
                x1 +=1

    for item in pointsPassed:
        for point in item:
            if(point[0] >= 2): 
                twoLines +=1
    print(twoLines)
main()