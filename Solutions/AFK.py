import sys
from collections import deque
import math


def input():
    return sys.stdin.readline().strip()


def bfs(s, e, grid):
    level = [math.inf]*(l*w)
    level[s[0]*l + s[1]] = 0
    q = deque([s])
    visited = [False]*(l*w)
    while q:
        a = q.popleft()
        x = a[0]*l + a[1]
        if a[1] + 2 <= l and grid[a[0]][a[1] + 1] != 'X' and not visited[x + 1]:
            level[x + 1] = level[x] + 1
            q.append([a[0], a[1] + 1])
            visited[x + 1] = True
        if a[1] - 1 >= 0 and grid[a[0]][a[1] - 1] != 'X' and not visited[x - 1]:
            level[x - 1] = level[x] + 1
            q.append([a[0], a[1] - 1])
            visited[x - 1] = True
        if a[0] + 2 <= w and grid[a[0] + 1][a[1]] != 'X' and not visited[x + l]:
            level[x + l] = level[x] + 1
            q.append([a[0] + 1, a[1]])
            visited[x + l] = True
        if a[0] - 1 >= 0 and grid[a[0] - 1][a[1]] != 'X' and not visited[x - l]:
            level[x - l] = level[x] + 1
            q.append([a[0] - 1, a[1]])
            visited[x - l] = True
    return level[e[0] * l + e[1]] if level[e[0] * l + e[1]] < 60 else '#notworth'


for i in range(int(input())):
    grid = []
    l, w = map(int, input().split())
    for j in range(w):
        grid.append(list(input()))
        if 'C' in grid[j]:
            s = [j, grid[j].index('C')]
        if 'W' in grid[j]:
            e = [j, grid[j].index('W')]
    print(bfs(s, e, grid))
