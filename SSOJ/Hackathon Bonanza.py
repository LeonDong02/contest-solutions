import sys
import heapq
input = sys.stdin.readline


def dijk(x):
    dist = [inf]*(n + 1)
    dist[x] = 0
    q = [x]
    while q:
        cur = heapq.heappop(q)
        for i in graph[cur]:
            if dist[i[1]] < dist[cur] + i[0]:
                dist[i[1]] = dist[cur] + i[0]
                heapq.heappush(q, i[1])
    return dist


inf = 9999999
n, m, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, z = map(int, input().split())
    graph[a].append([z, b])
    graph[b].append([z, a])
memo = {}
for _ in range(q):
    a, b = map(int, input().split())
    if a in memo:
        print(memo[a][b] if memo[a][b] != inf else -1)
    else:
        memo[a] = dijk(a)
        print(memo[a][b] if memo[a][b] != inf else -1)