import sys


def input():
    return sys.stdin.readline().strip()


def connected(x):
    global visited
    if x not in visited:
        visited.append(x)
        for i in graph[x]:
            connected(i)


graph = {}
visited = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x not in graph:
        graph[x] = []
    graph[x].append(y)
a, b = map(int, input().split())
connected(a)
print('Tangled' if b in visited else 'Not Tangled')
