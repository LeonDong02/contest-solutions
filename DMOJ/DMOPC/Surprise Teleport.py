import sys
from collections import deque
import math


def input():
    return sys.stdin.readline().strip()


def bfs(s, e):
    level = [math.inf]*(r*c)
    level[s[0]*c + s[1]] = 0
    q = deque([s])
    visited = [False]*(r*c)
    visited[s[0]*c + s[1]] = True
    while q:
        a = q.popleft()
        x = a[0] * c + a[1]
        if a[1] + 2 <= c and grid[a[0]][a[1] + 1] != 'X' and not visited[x + 1]:
            level[x + 1] = level[x] + 1
            q.append([a[0], a[1] + 1])
            visited[x + 1] = True
        if a[1] - 1 >= 0 and grid[a[0]][a[1] - 1] != 'X' and not visited[x - 1]:
            level[x - 1] = level[x] + 1
            q.append([a[0], a[1] - 1])
            visited[x - 1] = True
        if a[0] + 2 <= r and grid[a[0] + 1][a[1]] != 'X' and not visited[x + c]:
            level[x + c] = level[x] + 1
            q.append([a[0] + 1, a[1]])
            visited[x + c] = True
        if a[0] - 1 >= 0 and grid[a[0] - 1][a[1]] != 'X' and not visited[x - c]:
            level[x - c] = level[x] + 1
            q.append([a[0] - 1, a[1]])
            visited[x - c] = True
    return level[e[0]*c + e[1]] - min(level[i[0]*c + i[1]] for i in tele)


grid = []
tele = []
r, c = map(int, input().split())
s = list(map(int, input().split()))
e = list(map(int, input().split()))
for _ in range(r):
    grid.append(list(input()))
tele = [list(map(int, input().split())) for _ in range(int(input()))]
print(bfs(s, e))
