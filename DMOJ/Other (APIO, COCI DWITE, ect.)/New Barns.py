import sys
input = sys.stdin.readline


def findparent(x):
    if x != parent[x]:
        return findparent(parent[x])
    return x


def findlca(u, v):
    if dep[u] < dep[v]:
        u, v = v, u
    for i in range(19, -1, -1):
        if lca[i][u] != -1 and dep[lca[i][u]] >= dep[v]:
            u = lca[i][u]
    if u == v:
        return u
    for i in range(19, -1, -1):
        if lca[i][u] != -1 and lca[i][v] != -1 and lca[i][u] != lca[i][v]:
            u = lca[i][u]
            v = lca[i][v]
    return lca[0][u]


def finddist(u, v, lcan):
    return dep[u] + dep[v] - (dep[lcan] * 2)


n = 0
q = int(input())
graph = [[]]
lca = [[] for _ in range(20)]
dep = [0]
vals = {}
parent = [0]
for i in range(20):
    lca[i].append(-1)
for _ in range(q):
    cur = input().split()
    que, ind = cur[0], int(cur[1])
    if que == 'B':
        n += 1
        if ind == -1:
            parent.append(n)
            vals[n] = [n, n, 0]
            graph.append([])
            dep.append(0)
            for i in range(20):
                lca[i].append(-1)
        else:
            parent.append(findparent(ind))
            graph.append([ind])
            graph[ind].append(n)
            dep.append(dep[ind] + 1)
            lca[0].append(ind)
            for i in range(1, 20):
                if lca[i - 1][n] != -1:
                    lca[i].append(lca[i - 1][lca[i - 1][n]])
                else:
                    lca[i].append(-1)
            lcauv, lcauw, lcavw = findlca(vals[parent[n]][0], vals[parent[n]][1]), findlca(vals[parent[n]][0], n), findlca(n, vals[parent[n]][1])
            dist1, dist2, dist3 = finddist(vals[parent[n]][0], vals[parent[n]][1], lcauv), finddist(vals[parent[n]][0], n, lcauw), finddist(n, vals[parent[n]][1], lcavw)
            if dist1 < dist2 or dist1 < dist3:
                if dist2 < dist3:
                    vals[parent[n]][0] = n
                    vals[parent[n]][2] = dist3
                else:
                    vals[parent[n]][1] = n
                    vals[parent[n]][2] = dist2
    elif que == 'Q':
        lca1, lca2 = findlca(ind, vals[parent[ind]][0]), findlca(ind, vals[parent[ind]][1])
        print(max(finddist(ind, vals[parent[ind]][0], lca1), finddist(ind, vals[parent[ind]][1], lca2)))
