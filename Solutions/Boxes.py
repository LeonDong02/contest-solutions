n = int(input())
size = [list(map(int, input().split())) for i in range(n)]
m = int(input())
lwh = [list(map(int, input().split())) for i in range(m)]
for i in range(m):
    lwh[i].sort()
    max = 0
    for j in range(n):
        size[j].sort()
        if size[j][0] >= lwh[i][0] and size[j][1] >= lwh[i][1] and size[j][2] >= lwh[i][2]:
            if max == 0: max = size[j][0] * size[j][1] * size[j][2]
            elif max > 0 and max > size[j][0] * size[j][1] * size[j][2]: max = size[j][0] * size[j][1] * size[j][2]
    if max == 0: print('Item does not fit.')
    else: print(max)