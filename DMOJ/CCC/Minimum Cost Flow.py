import sys
input = sys.stdin.readline


def gp(x):
    while x != p[x]:
        x = p[x]
    return x


n, m, d = map(int, input().split())
edges = []
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    edges.append([a, b, c, 0])
for _ in range(m - n + 1):
    a, b, c = map(int, input().split())
    edges.append([a, b, c, 1])
edges.sort(key=lambda x: x[2])
p = [i for i in range(n + 1)]
r = [1 for _ in range(n + 1)]
mst = []
for edge in edges:
    a, b = gp(edge[0]), gp(edge[1])
    if a != b:
        if r[a] > r[b]:
            p[b] = a
        elif r[b] > r[a]:
            p[a] = b
        else:
            p[a] = b
            r[b] += 1
        mst.append(edge)
ans = sum(mst[i][3] for i in range(n - 1))
if mst[-1][3] and d:
    p = [i for i in range(n + 1)]
    r = [1 for i in range(n + 1)]
    for edge in edges:
        a, b = gp(edge[0]), gp(edge[1])
        if a != b:
            if edge[2] < mst[-1][2] or (edge[2] == mst[-1][2] and not edge[3]):
                if r[a] > r[b]:
                    p[b] = a
                elif r[b] > r[a]:
                    p[a] = b
                else:
                    p[a] = b
                    r[b] += 1
            elif not edge[3] and edge[2] <= d:
                ans -= 1
                break
print(ans)
