import sys
import math


def input():
    return sys.stdin.readline().strip()


def bfs(s):
    dist = [math.inf] * (n + 1)
    dist[s] = 0
    nodes = [True]*(n + 1)
    while nodes:
        min_node = None
        for i in range(1, n + 1):
            if nodes[i]:
                if min_node is None:
                    min_node = i
                elif dist[i] < dist[min_node]:
                    min_node = i
        if min_node is None:
            break
        nodes[min_node] = False
        for i in graph[min_node]:
            if nodes[i[1]]:
                weight = dist[min_node] + i[0]
                if weight < dist[i[1]]:
                    dist[i[1]] = weight
    return dist


n, m, b, q = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([z, y])
    graph[y].append([z, x])
distance = bfs(b)
for _ in range(q):
    cur = distance[int(input())]
    print(cur if not math.isinf(cur) else -1)
