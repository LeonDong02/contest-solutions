import sys


def input():
    return sys.stdin.readline().strip()


def bfs(x):
    dist = [inf]*(n + 1)
    dist[x] = 0
    nodes = [i + 1 for i in range(n)]
    while nodes:
        min_node = None
        cur = None
        for i in range(len(nodes)):
            if min_node is None:
                min_node = nodes[i]
                cur = i
            elif dist[nodes[i]] < dist[min_node]:
                min_node = nodes[i]
                cur = i
        if min_node is None:
            break
        del(nodes[cur])
        for i in range(1, n + 1):
            if graph[min_node][i] != 999999999999:
                weight = dist[min_node] + graph[min_node][i]
                if weight < dist[i]:
                    dist[i] = weight
    return dist


inf = 999999999999
n = int(input())
graph = [[inf for i in range(n + 1)] for j in range(n + 1)]
for _ in range(int(input())):
    x, y, c = map(int, input().split())
    graph[x][y] = c
    graph[y][x] = c
z, p = [], []
for _ in range(int(input())):
    a, b = map(int, input().split())
    z.append(a)
    p.append(b)
e = bfs(int(input()))
print(min(e[z[i]] + p[i] for i in range(len(z))))
