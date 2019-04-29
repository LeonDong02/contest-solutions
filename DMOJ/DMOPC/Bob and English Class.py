import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(5000000)


def dfs(cur, parent):
    for i in graph[cur]:
        if i[0] != parent:
            size[cur] += dfs(i[0], cur)
    return size[cur]


def findcent(cur, parent):
    for i in graph[cur]:
        if size[i[0]] > k // 2 and i[0] != parent:
            return findcent(i[0], cur)
    return cur


def bfs(s):
    dist = [-1] * (n + 1)
    dist[s] = 0
    q = deque([s])
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if dist[i[0]] == -1:
                dist[i[0]] = dist[cur] + i[1]
                q.append(i[0])
    return dist


k, n = map(int, input().split())
student, size = [0] * (n + 1), [0] * (n + 1)
for i in list(map(int, input().split())):
    student[i] += 1
    size[i] += 1
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, d = map(int, input().split())
    graph[a].append([b, d])
    graph[b].append([a, d])
cur = n // 2
dfs(cur, cur)
dist = bfs(findcent(cur, cur))
c = 0
for i in range(1, n + 1):
    c += dist[i] * student[i]
print(c)
