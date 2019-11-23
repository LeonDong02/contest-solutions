import sys, math
input = sys.stdin.readline

def constructutil(a, s, e, tree, ind):
    if s == e:
        tree[ind] = a[s]
    else:
        mid = (s + e) // 2
        tree[ind] = constructutil(a, s, mid, tree, 2 * ind + 1) + constructutil(a, mid + 1, e, tree, 2 * ind + 2)
    return tree[ind]

def construct(a, n):
    maxs = 2 * pow(2, int(math.ceil(math.log(n, 2)))) - 1
    tree = [0] * maxs
    lazy = [0] * maxs
    constructutil(a, 0, n - 1, tree, 0)
    return tree, lazy


def updaterangeutil(si, ss, se, us, ue, diff):
    cur = si * 2
    curn = [cur + 1, cur + 2]
    if lazy[si]:
        tree[si] += (se - ss + 1) * lazy[si]
        if ss != se:
            lazy[curn[0]] += lazy[si]
            lazy[curn[1]] += lazy[si]
        lazy[si] = 0
    if ss > se or ss > ue or se < us:
        return
    if ss >= us and se <= ue:
        tree[si] += (se - ss + 1) * diff
        if ss != se:
            lazy[curn[0]] += diff
            lazy[curn[1]] += diff
        return
    mid = (ss + se) // 2
    updaterangeutil(curn[0], ss, mid, us, ue, diff)
    updaterangeutil(curn[1], mid + 1, se, us, ue, diff)
    tree[si] = tree[curn[0]] + tree[curn[1]]

def updaterange(n, us, ue, diff):
    updaterangeutil(0, 0, n - 1, us, ue, diff)


def getsumutil(ss, se, qs, qe, si):
    cur = si * 2
    curn = [cur + 1, cur + 2]
    if lazy[si]:
        tree[si] += (se - ss + 1) * lazy[si]
        if ss != se:
            lazy[curn[0]] += lazy[si]
            lazy[curn[1]] += lazy[si]
        lazy[si] = 0
    if ss > se or ss > qe or se < qs:
        return 0
    if ss >= qs and se <= qe:
        return tree[si]
    mid = (ss + se) // 2
    return getsumutil(ss, mid, qs, qe, curn[0]) + getsumutil(mid + 1, se, qs, qe, curn[1])

def getsum(n, s, e):
    if s < 0 or e > n - 1 or s > e:
        return -1
    return getsumutil(0, n - 1, s, e, 0)


m, n, q = map(int, input().split())
a = list(map(int, input().split()))
tree, lazy = construct(a, n)
for _ in range(q):
    cur = list(map(int, input().split()))
    if cur[0] == 1:
        updaterange(n, cur[1] - 1, cur[2] - 1, cur[3])
    elif cur[0] == 2:
        sys.stdout.write(str(getsum(n, cur[1] - 1, cur[2] - 1) % m))
