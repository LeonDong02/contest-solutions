import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(a, b):
    visited = [a]
    q = deque([a])
    while q:
        x = q.popleft()
        if x == b:
            return True
        for i in graph[x]:
            if i not in visited:
                visited.append(i)
                q.append(i)
    return False


n, m = map(int, input().split())
graph = {}
for i in range(m):
    x, y = map(int, input().split())
    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []
    graph[x].append(y)
p, q = map(int, input().split())
if bfs(p, q):
    print('yes')
elif bfs(q, p):
    print('no')
else:
    print('unknown')
