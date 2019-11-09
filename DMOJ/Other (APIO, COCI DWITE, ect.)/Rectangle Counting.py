input = __import__("sys").stdin.readline

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


size = 1000006
n = int(input())
coord = [list(map(int, input().split())) for _ in range(n)]
event = []
for i in range(n):
    event.append([coord[i][0], coord[i][1], coord[i][3], 1]) #x, lo, hi, flag
    event.append([coord[i][2], coord[i][1], coord[i][3], -1])
event.sort(key=lambda x: x[0], reverse=True)
hi, lo = [0] * size, [0] * size
c = 0
while len(event):
    cur = [event.pop()]
    while len(event) and event[-1][0] == cur[0][0]:
        cur.append(event.pop())
    cur.sort(key=lambda x: x[-1], reverse=True)
    while len(cur):
        go = cur.pop()
        if go[3] == -1:
            c += getsum(lo, go[2] - 1) - getsum(hi, go[1]) - 1
        update(hi, size, go[2], go[3])
        update(lo, size, go[1], go[3])
print(c)
