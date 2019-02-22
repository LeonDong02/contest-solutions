import sys
import heapq
input = sys.stdin.readline


def dijk(s):
    dist = [999999999999]*(n + 1)
    dist[0] = 0
    dist[s] = 0
    h = [s]
    far = s
    while h:
        cur = heapq.heappop(h)
        for i in graph[cur]:
            w = dist[cur] + i[0]
            if w < dist[i[1]]:
                dist[i[1]] = w
                if dist[i[1]] > dist[far]:
                    far = i[1]
                heapq.heappush(h, i[1])
    return dist, far


n, t = map(int, input().split())
graph = [[] for _ in range(n + 1)]
weight = 0
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
    weight += c
lev1, cur = dijk(1)
lev2, cur = dijk(cur)
lev3, cur = dijk(cur)
for i in range(1, n + 1):
    if len(graph[i]) == t:
        print(i, 2*weight - max(lev2[i], lev3[i]))
