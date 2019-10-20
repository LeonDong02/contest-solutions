import sys
input = sys.stdin.readline


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
d = int(input())
curd = abs(x1 - x2) + abs(y1 - y2)
if curd == 1:
    if d == 1:
        print(0)
    else:
        print('impossible')
    sys.exit()
elif curd % 2 != d % 2 or d < curd:
    print('impossible')
    sys.exit()
n = (d - curd) // 2
coord = []
if (x1 + 1 == x2 and y1 + 1 == y2) or (x1 + 1 == x2 and y1 - 1 == y2) or (x1 - 1 == x2 and y1 + 1 == y2) or (x1 - 1 == x2 and y1 - 1 == y2):
    if d == 4:
        print('impossible')
        sys.exit()
    n -= 1
    if x1 > x2 and y1 > y2:
        for i in range(n):
            coord.append([x1 - 1, y1 + i])
        for i in range(n):
            coord.append([x1 + i, y1 - 1])
    elif x1 > x2 and y1 < y2:
        for i in range(n):
            coord.append([x1 + i, y1 + 1])
        for i in range(n):
            coord.append([x1 - 1, y1 - i])
    elif x1 < x2 and y1 > y2:
        for i in range(n):
            coord.append([x1 + 1, y1 + i])
        for i in range(n):
            coord.append([x1 - i, y1 - 1])
    elif x1 < x2 and y1 < y2:
        for i in range(n):
            coord.append([x1 - i, y1 + 1])
        for i in range(n):
            coord.append([x1 + 1, y1 - i])
elif x1 > x2 and y1 > y2:
    for i in range(n):
        coord.append([x1 - 1, y1 + i])
    for i in range(n):
        coord.append([x1 + i, y1 - 1])
elif x1 > x2 and y1 < y2:
    for i in range(n):
        coord.append([x1 + i, y1 + 1])
    for i in range(n):
        coord.append([x1 - 1, y1 - i])
elif x1 < x2 and y1 > y2:
    for i in range(n):
        coord.append([x1 + 1, y1 + i])
    for i in range(n):
        coord.append([x1 - i, y1 - 1])
elif x1 < x2 and y1 < y2:
    for i in range(n):
        coord.append([x1 - i, y1 + 1])
    for i in range(n):
        coord.append([x1 + 1, y1 - i])
elif x1 == x2 and y1 > y2:
    for i in range(n):
        coord.append([x1 + i, y1 - 1])
    for i in range(1, n + 1):
        coord.append([x1 - i, y1 - 1])
elif x1 == x2 and y1 < y2:
    for i in range(n):
        coord.append([x1 + i, y1 + 1])
    for i in range(1, n + 1):
        coord.append([x1 - i, y1 + 1])
elif x1 > x2 and y1 == y2:
    for i in range(n):
        coord.append([x1 - 1, y1 - i])
    for i in range(1, n + 1):
        coord.append([x1 - 1, y1 + i])
elif x1 < x2 and y1 == y2:
    for i in range(n):
        coord.append([x1 + 1, y1 - i])
    for i in range(1, n + 1):
        coord.append([x1 + 1, y1 + i])
if len(coord) > 10000:
    print('impossible')
    sys.exit()
print(len(coord))
for i in coord:
    print(i[0], i[1])