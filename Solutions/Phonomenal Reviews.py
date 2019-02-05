import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def prune(x):
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            prune(i)
            mark[x] += mark[i]


def bfs(x):
    v = [False]*n
    v[x] = True
    dist = [0]*n
    q = deque([x])
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not v[i] and mark[i]:
                v[i] = True
                q.append(i)
                dist[i] = dist[cur] + 1
    return dist


n, m = map(int, input().split())
pho = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
mark = [0]*n
for i in pho:
    mark[i] = 1
visited = [False]*n
visited[pho[0]] = True
prune(pho[0])
nodes = n - mark.count(0) - 1
lev = bfs(pho[0])
lev = bfs(lev.index(max(lev)))
print(2*nodes - max(lev))
