import sys
input = sys.stdin.readline


def gp(x):
    while x != p[x]:
        x = p[x]
    return x


m = int(input())
edges = [{} for _ in range(m)]
for i in range(m):
    cur = list(map(int, input().split()))
    e = cur[0]
    for j in range(1, e + 1):
        edge = [min(cur[j], cur[(j % e) + 1]), max(cur[j], cur[(j % e) + 1])]
        edges[i][' '.join(list(map(str, edge)))] = cur[j + e]
newedges1, newedges2 = [], []
for i in range(m):
    for j in edges[i]:
        found = False
        for k in range(i + 1, m):
            for l in edges[k]:
                if j == l:
                    newedges1.append([i, k, edges[i][j]])
                    newedges2.append([i, k, edges[i][j]])
                    del edges[k][l]
                    found = True
                if found:
                    break
        if not found:
            newedges2.append([i, m, edges[i][j]])
newedges1.sort(key=lambda x: x[2])
newedges2.sort(key=lambda x: x[2])
p = [i for i in range(m + 1)]
ans1 = 0
for i in newedges1:
    a, b = gp(i[0]), gp(i[1])
    if a != b:
        p[a] = b
        ans1 += i[2]
p = [i for i in range(m + 1)]
ans2 = 0
for i in newedges2:
    a, b = gp(i[0]), gp(i[1])
    if a != b:
        p[a] = b
        ans2 += i[2]
print(min(ans1, ans2))
