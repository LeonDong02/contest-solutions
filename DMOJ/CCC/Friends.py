import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(x, y):
    dist = [-1 for i in range(len(graph) + 1)]
    q = deque([x])
    c = 0
    while q:
        c += 1
        a = q.popleft()
        for i in graph[a]:
            if i == y:
                return dist[c - 1] + 1
            if i != x:
                dist[c] = dist[c - 1] + 1
                q.append(i)
            else:
                break
    return -1


graph = {}
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []
    graph[x].append(y)
x, y = map(int, input().split())
while x or y:
    sep = bfs(x, y)
    print('Yes ' + str(sep) if sep != -1 else 'No')
    x, y = map(int, input().split())
