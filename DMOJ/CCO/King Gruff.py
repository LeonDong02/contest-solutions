import sys
import bisect
from collections import deque
input = sys.stdin.readline


def dijk(x, graph):
    dist = [9999999999]*(n + 1)
    dist[x] = 0
    visited = [False]*(n + 1)
    q = deque([x])
    while q:
        cur = q.popleft()
        visited[cur] = False
        for i in graph[cur]:
            if dist[cur] + i[1] < dist[i[0]]:
                dist[i[0]] = dist[cur] + i[1]
                if not visited[i[0]]:
                    visited[i[0]] = True
                    q.append(i[0])
    return dist


n, m, a, b = map(int, input().split())
graph = [[] for _ in range(n + 1)]
invgraph = [[] for _ in range(n + 1)]
costs = []
for i in range(m):
    x, y, l, c = map(int, input().split())
    graph[x].append([y, l, c])
    invgraph[y].append([x, l, c])
    costs.append(c)
dist = dijk(a, graph)
distend = dijk(b, invgraph)
minpath = []
for i in range(1, n + 1):
    if dist[i] < 9999999999:
        for j in graph[i]:
            minpath.append([dist[i] + j[1] + distend[j[0]], j[2]])
minpath.sort()
mindist, mincost = [0], [0]
m = len(minpath)
minpath = deque(minpath)
for i in range(m):
    cur = minpath.popleft()
    mindist.append(cur[0])
    mincost.append(cur[1] + mincost[-1])
for _ in range(int(input())):
    d = int(input())
    print(mincost[bisect.bisect_right(mindist, d) - 1])
