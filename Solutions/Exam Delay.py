import sys
import math


def input():
    return sys.stdin.readline().strip()


def bfs(x):
    dist = [math.inf]*(v + 1)
    dist[x] = 0
    dists = [math.inf]*(v + 1)
    dists[x] = 0
    nodes = [i + 1 for i in range(v)]
    path = [0]*(v + 1)
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
        for i in graph[min_node]:
            weight = dist[min_node] + (i[0]/i[1]*60)
            weights = dists[min_node] + (i[0]/i[1]*80)
            if weight < dist[i[2]]:
                dist[i[2]] = weight
                dists[i[2]] = weights
                path[i[2]] = path[min_node] + 1
    return path[v], int(round(dists[v] - dist[v], 0))


v, e = int(input()), int(input())
graph = {i: [] for i in range(1, v + 1)}
for _ in range(e):
    m, n, d, s = map(int, input().split())
    graph[m].append([d, s, n])
    graph[n].append([d, s, m])
a, b = bfs(1)
print(a)
print(b)
