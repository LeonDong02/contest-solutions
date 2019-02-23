import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(x):
    dist = [-1]*(r*c)
    dist[x[0]*c + x[1]] = 1
    visited = [False]*(r*c)
    q = deque([x])
    while q:
        a = q.popleft()
        x = a[0]*c + a[1]
        if grid[a[0]][a[1]] == '-' or grid[a[0]][a[1]] == '+':
            if a[1] + 2 <= c and grid[a[0]][a[1] + 1] != '*' and not visited[x + 1]:
                dist[x + 1] = dist[x] + 1
                q.append([a[0], a[1] + 1])
                visited[x + 1] = True
            if a[1] - 1 >= 0 and grid[a[0]][a[1] - 1] != '*' and not visited[x - 1]:
                dist[x - 1] = dist[x] + 1
                q.append([a[0], a[1] - 1])
                visited[x - 1] = True
        if grid[a[0]][a[1]] == '|' or grid[a[0]][a[1]] == '+':
            if a[0] + 2 <= r and grid[a[0] + 1][a[1]] != '*' and not visited[x + c]:
                dist[x + c] = dist[x] + 1
                q.append([a[0] + 1, a[1]])
                visited[x + c] = True
            if a[0] - 1 >= 0 and grid[a[0] - 1][a[1]] != '*' and not visited[x - c]:
                dist[x - c] = dist[x] + 1
                q.append([a[0] - 1, a[1]])
                visited[x - c] = True
    return dist[(r - 1)*c + (c - 1)]


for i in range(int(input())):
    grid = []
    r, c = int(input()), int(input())
    for i in range(r):
        grid.append(list(input()))
    print(bfs([0, 0]))
