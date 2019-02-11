import sys
from collections import deque
input = sys.stdin.readline


def bfs(x):
    dist = [-1]*(n + 1)
    dist[x] = 1
    visited = [False]*(n + 1)
    visited[x] = True
    q = deque([x])
    far = x
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                dist[i] = dist[a] + 1
                if dist[far] < dist[i]:
                    far = i
    return dist, far


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
lev1, cur = bfs(1)
lev2, cur = bfs(cur)
lev3, cur = bfs(cur)
for i in range(1, n + 1):
    print(max(lev2[i], lev3[i]))
