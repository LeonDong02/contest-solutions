import sys
from collections import deque
input = sys.stdin.readline


def dist(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**(1/2)


start = list(map(int, input().split()))
end = list(map(int, input().split()))
mindist = dist(start[0], start[1], start[2], end[0], end[1], end[2])
cur = [1, 2, 3]
dir = [1, 1, 1]
dirc = [0, 0]
x, y = input().split()
while y != 'E':
    for i in range(int(x)):
        start[cur[0] - 1] += dir[cur[0] - 1]
        curdist = dist(start[0], start[1], start[2], end[0], end[1], end[2])
        mindist = curdist if curdist < mindist else mindist
        if mindist == 0:
            break
    if y in 'LR':
        cur[0], cur[1] = cur[1], cur[0]
        if y == 'L':
            dirc[0] += 1
        elif y == 'R':
            dirc[0] -= 1
        if not (0 <= dirc[0] <= 1):
            dir[cur[0] - 1] *= -1
            dir[cur[1] - 1] *= -1
            dirc[0] = 0 if dirc[0] == 2 else 1
    if y in 'UD':
        cur[0], cur[2] = cur[2], cur[0]
        if y == 'U':
            dirc[1] += 1
        elif y == 'D':
            dirc[1] -= 1
        if not (0 <= dirc[1] <= 1):
            dir[cur[0] - 1] *= -1
            dir[cur[2] - 1] *= -1
            dirc[1] = 0 if dirc[1] == 2 else 1
    x, y = input().split()
for i in range(int(x)):
    start[cur[0] - 1] += dir[cur[0] - 1]
    curdist = dist(start[0], start[1], start[2], end[0], end[1], end[2])
    mindist = curdist if curdist < mindist else mindist
    if mindist == 0:
        break
print(round(mindist, 2))
