import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(s):
    if s == 1:
        for i in v:
            if q[i]:
                print('inf')
                sys.exit()
    if q[s]:
        v.append(s)
    if c[s]:
        q[s] = False
        return c[s]
    q[s] = True
    c[s] = sum(dfs(i) for i in graphinv[s])
    q[s] = False
    return c[s]


n, m = map(int, input().split())
graphinv = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graphinv[b].append(a)
c = [0] * (n + 1)
c[1] = 1
q = [False] * (n + 1)
v = []
print(''.join(list(map(str, list(str(dfs(2)))))[-9:]))