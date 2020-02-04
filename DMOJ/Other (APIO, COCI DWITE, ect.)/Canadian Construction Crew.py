import sys
input = sys.stdin.readline


def getp(x):
    while x != p[x]:
        x = p[x]
    return x


def getb(v):
    if v:
        return True
    return False


n, q = map(int, input().split())
p = [i for i in range(n + 1)]
g = [{} for _ in range(n)]
d = [False] * n
oddcount = 0
remap = {}
needconnect = [False] * n
needconnectcount = 0
ind = 0
for i in range(q):
    done = False
    a, b, x = map(int, input().split())
    if a not in remap:
        remap[a] = ind
        ind += 1
    if b not in remap:
        remap[b] = ind
        ind += 1
    a, b = remap[a], remap[b]
    p1, p2 = getp(a), getp(b)
    if p1 > p2:
        p1, p2 = p2, p1
    if p1 != p2:
        p[p2] = p1
        if p1 and not needconnect[p1]:
            needconnect[p1] = True
            needconnectcount += 1
        elif not p1 and needconnect[p2]:
            needconnect[p2] = False
            needconnectcount -= 1
        elif p1 and needconnect[p2]:
            if needconnect[p1]:
                needconnectcount -= 1
            needconnect[p2] = False
            needconnect[p1] = True
    if needconnectcount:
        print('NO')
        done = True
    if a > b:
        a, b = b, a
    if b not in g[a]:
        g[a][b] = 0
    cur = g[a][b]
    g[a][b] = (g[a][b] + x) & 1
    if getb(cur) != getb(g[a][b]):
        d[a], d[b] = not d[a], not d[b]
        if d[a]:
            oddcount += 1
        else:
            oddcount -= 1
        if d[b]:
            oddcount += 1
        else:
            oddcount -= 1
    if not done:
        if oddcount == 0 or oddcount == 2:
            print('YES')
        else:
            print('NO')
