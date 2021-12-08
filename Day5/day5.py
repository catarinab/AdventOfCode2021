def main():
    f = open("input.txt", "r")
    lines = f.readlines(); points = []
    for i in range(0, len(lines)): points.append(lines[i].strip().split(' '))
    print(points)
main()