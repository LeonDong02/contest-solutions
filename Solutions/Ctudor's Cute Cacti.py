import sys
input = sys.stdin.readline


n, q = map(int, input().split())
x, y = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
que = {}
for _ in range(q):
    t, i, j = map(int, input().split())
    if t == 1:
        x[i] += 1
        y[j] += 1
        if str([i, j]) not in que:
            que[str([i, j])] = 0
        que[str([i, j])] += 1
    if t == 2:
        cur = x[i] + y[j]
        if str([i, j]) in que:
            cur += que[str([i, j])]
        print(cur%2)
