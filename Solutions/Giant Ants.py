import sys
from collections import deque
import math


def input():
    return sys.stdin.readline().strip()


def bfs(x):
    dist = [-1]*(n + 1)
    dist[x] = 0
    visited = [False]*(n + 1)
    visited[x] = True
    q = deque([x])
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i] and dist[a] < antdist[i]:
                visited[i] = True
                q.append(i)
                dist[i] = dist[a] + 1
    return dist[n] if dist[n] > -1 else 'sacrifice bobhob314'



n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
ant = [int(input()) for i in range(int(input()))]
antdist = [math.inf]*(n + 1)
visited = [False]*(n + 1)
q = deque([])
for i in ant:
    antdist[i] = 0
    visited[i] = True
    q.append(i)
while q:
    a = q.popleft()
    for i in graph[a]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
            if antdist[a] + 4 < antdist[i]:
                antdist[i] = antdist[a] + 4
print(bfs(1))
