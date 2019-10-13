import sys
input = sys.stdin.readline


def getsum(tree, i):
    s = 0
    i += 1
    while i > 0:
        s += tree[i]
        i -= i & (-i)
    return s


def update(tree, n, i, v):
    i += 1
    while i <= n:
        tree[i] += v
        i += i & (-i)


def construct(a, n):
    tree = [0] * (n + 1)
    for i in range(n):
        update(tree, n, i, a[i])
    return tree


n, m = map(int, input().split())
g = list(map(int, input().split()))
count = [[0 for _ in range(n)] for _ in range(21)]
for i in range(n):
    count[g[i]][i] = 1
tree = [construct(count[i], n) for i in range(21)]
for _ in range(m):
    cur = list(map(int, input().split()))
    if cur[0] == 1:
        a, b = cur[1], cur[2]
        update(tree[g[a - 1]], n, a - 1, -1)
        update(tree[b], n, a - 1, 1)
        g[a - 1] = b
    elif cur[0] == 2:
        l, r, c = cur[1], cur[2], cur[3]
        cur = [getsum(tree[i], r - 1) - getsum(tree[i], l - 2) for i in range(21)]
        ind = 20
        while c:
            c -= min(c, cur[ind])
            ind -= 1
        print(ind + 1)