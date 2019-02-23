import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(rem):
    visited = [True] + [False]*25
    q = deque([0])
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                if [chr(cur + 65), chr(i + 65)] != rem and [chr(i + 65), chr(cur + 65)] != rem:
                    q.append(i)
                    visited[i] = True
    if all(visited[i] for i in nodes):
        return False
    return True


graph = [[] for _ in range(26)]
edges, nodes = [], []
xy = list(input())
while xy[0] != '*':
    graph[ord(xy[0]) - 65].append(ord(xy[1]) - 65)
    graph[ord(xy[1]) - 65].append(ord(xy[0]) - 65)
    edges.append(xy)
    if ord(xy[0]) - 65 not in nodes:
        nodes.append(ord(xy[0]) - 65)
    if ord(xy[1]) - 65 not in nodes:
        nodes.append(ord(xy[1]) - 65)
    xy = list(input())
c = 0
for i in edges:
    if bfs(i):
        print(i[0] + i[1])
        c += 1
print('There are', c, 'disconnecting roads.')
