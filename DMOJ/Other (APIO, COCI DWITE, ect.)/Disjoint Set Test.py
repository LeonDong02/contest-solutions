import sys
input = sys.stdin.readline


def parent(x):
    c = x
    while c != p[c]:
        c = p[c]
    while x != c:
        x, p[x] = p[x], c
    return c


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
p = [i for i in range(n + 1)]
mst = []
for ind in range(m):
    x, y = parent(edges[ind][0]), parent(edges[ind][1])
    if x != y:
        p[x] = y
        mst.append(str(ind + 1))
print('\n'.join(mst) if len(mst) == n - 1 else 'Disconnected Graph')
print(p)
