import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def bfs(x):
    level = {x: 0}
    q = deque([x])
    visited = [x]
    while q:
        a = q.popleft()
        for i in graph[a]:
            if i not in visited:
                level[i] = level[a] + 1
                q.append(i)
                visited.append(i)
    if 'Waterloo GO' in level:
        return level['Waterloo GO']
    else:
        return 'RIP ACE'


n, t = map(int, input().split())
graph = {'home': [], 'Waterloo GO': []}
for i in range(n):
    graph[input()] = []
for i in range(t):
    s, e = input().split('-')
    graph[s].append(e)
    graph[e].append(s)
print(bfs('home'))
