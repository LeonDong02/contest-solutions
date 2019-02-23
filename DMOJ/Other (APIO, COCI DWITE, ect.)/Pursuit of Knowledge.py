import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


memo = {}


def bfs(x, y):
    if x in memo:
        return memo[x][y]*t if memo[x][y] > 0 else 'Not enough hallways!'
    dist = [-1]*(n + 1)
    dist[x] = 0
    visited = [False]*(n + 1)
    visited[x] = True
    q = deque([x])
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                dist[i] = dist[a] + 1
    memo[x] = dist
    return dist[y]*t if dist[y] > 0 else 'Not enough hallways!'


n, m, t = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
for i in range(int(input())):
    x, y = map(int, input().split())
    print(bfs(x, y))
