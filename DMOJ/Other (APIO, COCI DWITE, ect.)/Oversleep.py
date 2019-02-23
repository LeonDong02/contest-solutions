import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(s, e):
    level = [-1]*(n*m)
    q = deque([s])
    visited = [False]*(n*m)
    while q:
        a = q.popleft()
        x = a[0] * m + a[1]
        if a[1] + 2 <= m and grid[a[0]][a[1] + 1] != 'X' and not visited[x + 1]:
            level[x + 1] = level[x] + 1
            q.append([a[0], a[1] + 1])
            visited[x + 1] = True
        if a[1] - 1 >= 0 and grid[a[0]][a[1] - 1] != 'X' and not visited[x - 1]:
            level[x - 1] = level[x] + 1
            q.append([a[0], a[1] - 1])
            visited[x - 1] = True
        if a[0] + 2 <= n and grid[a[0] + 1][a[1]] != 'X' and not visited[x + m]:
            level[x + m] = level[x] + 1
            q.append([a[0] + 1, a[1]])
            visited[x + m] = True
        if a[0] - 1 >= 0 and grid[a[0] - 1][a[1]] != 'X' and not visited[x - m]:
            level[x - m] = level[x] + 1
            q.append([a[0] - 1, a[1]])
            visited[x - m] = True
    return level[e[0] * m + e[1]]


grid = []
n, m = map(int, input().split())
for i in range(n):
    grid.append(list(input()))
    if 's' in grid[i]:
        s = [i, grid[i].index('s')]
    if 'e' in grid[i]:
        e = [i, grid[i].index('e')]
print(bfs(s, e))
