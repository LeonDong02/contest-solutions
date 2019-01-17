import sys


def input():
    return sys.stdin.readline().strip()


def kruskal():
    mst = []
    parent = [i for i in range(n + 1)]
    rank = [1 for _ in range(n + 1)]

    def get_parent(x):
        if x != parent[x]:
            parent[x] = get_parent(parent[x])
        return parent[x]

    c = 0
    for edge in edges:
        xroot = get_parent(edge[1])
        yroot = get_parent(edge[2])
        if xroot != yroot:
            if rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            elif rank[yroot] > rank[xroot]:
                parent[xroot] = yroot
            else:
                parent[xroot] = yroot
                rank[yroot] += 1
            mst.append(edge)
            if not edge[3]:
                c += 1
    if not mst[-1][3]:
        parent = [i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]
        for edge in edges:
            xroot = get_parent(edge[1])
            yroot = get_parent(edge[2])
            if xroot != yroot:
                if edge[0] < mst[-1][0] or (edge[0] == mst[-1][0] and edge[3]):
                    if rank[xroot] > rank[yroot]:
                        parent[yroot] = xroot
                    elif rank[yroot] > rank[xroot]:
                        parent[xroot] = yroot
                    else:
                        parent[xroot] = yroot
                        rank[yroot] += 1
                elif edge[3] and edge[0] <= d:
                    c -= 1
                    return c
    return c


n, m, d = map(int, input().split())
edges = []
for i in range(n - 1):
    a, b, c = map(int, input().split())
    edges.append([c, a, b, True])
for i in range(m + 1 - n):
    a, b, c = map(int, input().split())
    edges.append([c, a, b, False])
edges.sort(key=lambda x: x[0])
print(kruskal())
