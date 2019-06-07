import sys
from collections import deque
sys.setrecursionlimit(50000)
input = sys.stdin.readline


def bfs(s):
    ind, longest= 0, 0
    dist = [0] * (n + 1)
    prev = [0] * (n + 1)
    q = deque([s])
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not dist[i] and i != s:
                if not prev[i]:
                    prev[i] = cur
                dist[i] = dist[cur] + 1
                if dist[i] > longest:
                    longest = dist[i]
                    ind = i
                q.append(i)
    return ind, longest, prev


def dfs(s, p, d):
    for i in graph[s]:
        if i != p:
            d = dfs(i, s, d)
            if d1[i] + graph[s][i] > d1[s]:
                d2[s], d1[s] = d1[s], d1[i] + graph[s][i]
            elif d1[i] + graph[s][i] > d2[s]:
                d2[s] = d1[i] + graph[s][i]
    return max(d, d1[s] + d2[s])


n, k = map(int, input().split())
graph = {i: {} for i in range(n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
d1, d2 = [0] * (n + 1), [0] * (n + 1)
ind, longest, prev = bfs(1)
ind, longest, prev = bfs(ind)
ans = 2 * (n - 1) - longest + 1
if k == 1:
    print(ans)
    sys.exit()
q = deque([ind])
while q:
    cur = q.popleft()
    graph[cur][prev[cur]] = -1
    graph[prev[cur]][cur] = -1
    if prev[cur]:
        q.append(prev[cur])
ans -= dfs(n // 2, 0, 0) - 1
print(ans)