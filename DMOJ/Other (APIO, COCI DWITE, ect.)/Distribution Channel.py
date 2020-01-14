import sys, math
input = sys.stdin.readline


def parent(x):
    c = x
    while c != p[c]:
        c = p[c]
    while x != c:
        x, p[x] = p[x], c
    return c


def dfs(st, p, w):
    lca[0][st] = p
    maxw[0][st] = w
    for i in graph[st]:
        if i[0] != p:
            dep[i[0]] = dep[st] + 1
            dfs(i[0], st, i[1])


def findlca(u, v):
    if dep[u] < dep[v]:
        u, v = v, u
    for i in range(len(lca) - 1, -1, -1):
        if lca[i][u] != -1 and dep[lca[i][u]] >= dep[v]:
            u = lca[i][u]
    if u == v:
        return u
    for i in range(len(lca) - 1, -1, -1):
        if lca[i][u] != -1 and lca[i][v] != -1 and lca[i][u] != lca[i][v]:
            u = lca[i][u]
            v = lca[i][v]
    return lca[0][u]


def findmaxw(v, curlca, cw):
    curmaxw = -1
    for i in range(len(lca) - 1, -1, -1):
        if lca[i][v] != -1 and dep[lca[i][v]] >= dep[curlca]:
            if maxw[i][v] != cw:
                curmaxw = max(curmaxw, maxw[i][v])
            v = lca[i][v]
    return curmaxw


n, m = map(int, input().split())
edges = list(sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x:x[2]))
used = [0] * m
graph = [[] for _ in range(n + 1)]
p = [i for i in range(n + 1)]
tot, c = 0, 0
for ind in range(m):
    i = edges[ind]
    x, y = parent(i[0]), parent(i[1])
    if x != y:
        p[x] = y
        graph[i[0]].append([i[1], i[2]])
        graph[i[1]].append([i[0], i[2]])
        tot += i[2]
        c += 1
        used[ind] = 1
    if c == n - 1:
        break
if c != n - 1:
    print(-1)
    sys.exit()
lca = [[-1] * (n + 1) for _ in range(int(math.log2(n + 1)) + 2)]
maxw = [[-1] * (n + 1) for _ in range(int(math.log2(n + 1)) + 2)]
dep = [0] * (n + 1)
dfs(1, -1, -1)
for i in range(1, len(lca)):
    for j in range(1, n + 1):
        if lca[i - 1][j] != -1:
            lca[i][j] = lca[i - 1][lca[i - 1][j]]
        if maxw[i - 1][j] != -1:
            maxw[i][j] = max(maxw[i - 1][lca[i - 1][j]], maxw[i - 1][j])
ans = []
for i in range(m):
    if not used[i]:
        a, b, w = edges[i][0], edges[i][1], edges[i][2]
        curlca = findlca(a, b)
        curmaxw = max(findmaxw(a, curlca, w), findmaxw(b, curlca, w))
        if curmaxw != -1 and curmaxw < w:
            ans.append(tot - curmaxw + w)
print(min(ans) if len(ans) else -1)
