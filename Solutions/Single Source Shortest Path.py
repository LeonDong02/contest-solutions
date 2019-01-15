import sys
import math
import heapq


def input():
    return sys.stdin.readline().strip()


def bfs(x):
    dist = [math.inf]*(n + 1)
    dist[x[1]] = 0
    h = [x]
    while h:
        a = heapq.heappop(h)
        for i in graph[a[1]]:
            d = dist[a[1]] + i[0]
            if d < dist[i[1]]:
                dist[i[1]] = d
                h.append([dist[i[1]], i[1]])
    return dist


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])
    graph[v].append([w, u])
x = bfs([0, 1])
for i in range(1, n + 1):
    print(x[i] if not math.isinf(x[i]) else -1)
