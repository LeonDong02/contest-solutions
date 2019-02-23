import sys
input = sys.stdin.readline


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
            c += edge[0]
    return c


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])
edges.sort(key=lambda x: x[0])
print(kruskal())
