import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(x):
    visited = [False]*(row*column)
    visited[x[0]*column + x[1]] = True
    dist = [-1]*(row*column)
    dist[x[0]*column + x[1]] = 0
    q = deque([x])
    while q:
        a = q.popleft()
        if grid[a[0]][a[1]] in 'LRUDS.':
            for i in range(4):
                cur = [a[0] + mr[i], a[1] + mc[i]]
                c = 0
                while grid[cur[0]][cur[1]] in 'LRUD':
                    if grid[cur[0]][cur[1]] == 'L' and not visited[cur[0]*column + cur[1]]:
                        visited[cur[0] * column + cur[1]] = True
                        cur = [cur[0], cur[1] - 1]
                    elif grid[cur[0]][cur[1]] == 'R' and not visited[cur[0]*column + cur[1]]:
                        visited[cur[0] * column + cur[1]] = True
                        cur = [cur[0], cur[1] + 1]
                    elif grid[cur[0]][cur[1]] == 'U' and not visited[cur[0]*column + cur[1]]:
                        visited[cur[0] * column + cur[1]] = True
                        cur = [cur[0] - 1, cur[1]]
                    elif grid[cur[0]][cur[1]] == 'D' and not visited[cur[0]*column + cur[1]]:
                        visited[cur[0] * column + cur[1]] = True
                        cur = [cur[0] + 1, cur[1]]
                    else:
                        break
                if 0 <= cur[0] < row and 0 <= cur[1] < column and not visited[cur[0]*column + cur[1]] and grid[cur[0]][cur[1]] in 'LRUD.':
                    visited[cur[0]*column + cur[1]] = True
                    q.append([cur[0], cur[1]])
                    dist[cur[0]*column + cur[1]] = dist[a[0]*column + a[1]] + 1
    return dist


grid = []
mc = [1, -1, 0, 0]
mr = [0, 0, 1, -1]
row, column = map(int, input().split())
open = []
camera = deque([])
for i in range(row):
    grid.append(list(input()))
    for j in range(column):
        if grid[i][j] == '.':
            open.append([i, j])
        if grid[i][j] == 'C':
            camera.append([i, j])
        if grid[i][j] == 'S':
            s = [i, j]
c = False
while camera:
    cam = camera.popleft()
    for i in reversed(range(cam[0])):
        if grid[i][cam[1]] == '.':
            grid[i][cam[1]] = 'M'
        if grid[i][cam[1]] == 'W':
            break
        if grid[i][cam[1]] == 'S':
            c = True
    for i in range(cam[0] + 1, row):
        if grid[i][cam[1]] == '.':
            grid[i][cam[1]] = 'M'
        if grid[i][cam[1]] == 'W':
            break
        if grid[i][cam[1]] == 'S':
            c = True
    for i in reversed(range(cam[1])):
        if grid[cam[0]][i] == '.':
            grid[cam[0]][i] = 'M'
        if grid[cam[0]][i] == 'W':
            break
        if grid[cam[0]][i] == 'S':
            c = True
    for i in range(cam[1] + 1, column):
        if grid[cam[0]][i] == '.':
            grid[cam[0]][i] = 'M'
        if grid[cam[0]][i] == 'W':
            break
        if grid[cam[0]][i] == 'S':
            c = True
x = bfs(s)
if not c:
    for i in open:
        print(x[i[0]*column + i[1]] if grid[i[0]][i[1]] != 'M' else -1)
else:
    for i in range(len(open)):
        print(-1)
