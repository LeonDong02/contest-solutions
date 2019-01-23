import sys
import math
import heapq


def input():
    return sys.stdin.readline().strip()


def dijk(s, e):
    dist = [[math.inf for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(k + 1):
        dist[s][i] = 0
    visited = [False]*(n + 1)
    h = [s]
    while h:
        cur = heapq.heappop(h)
        visited[cur] = False
        for i in graph[cur]:
            for j in range(k - i[2] + 1):
                if dist[i[0]][j + i[2]] > dist[cur][j] + i[1]:
                    dist[i[0]][j + i[2]] = dist[cur][j] + i[1]
                    if not visited[i[0]]:
                        heapq.heappush(h, i[0])
                        visited[i[0]] = True
    return dist[e][k - 1] if not math.isinf(dist[e][k - 1]) else -1


k, n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b, t, h = map(int, input().split())
    graph[a].append([b, t, h])
    graph[b].append([a, t, h])
a, b = map(int, input().split())
print(dijk(a, b))
