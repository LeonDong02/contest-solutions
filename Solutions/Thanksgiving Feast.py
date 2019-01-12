import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(x):
    q = deque([x])
    visited = [False]*(n + 1)
    visited[x] = True
    dist = [-1]*(n + 1)
    dist[x] = 0
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                dist[i] = dist[a] + 1
    return dist


n, m, k, a, b = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
gift = list(map(int, input().split()))
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
adist = bfs(a)
bdist = bfs(b)
print(min(adist[i] + bdist[i] for i in gift))
