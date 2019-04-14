input = __import__("sys").stdin.readline


n, m = map(int, input().split())
a = list(sorted(list(map(int, input().split()))))
c = 0
lp, rp = 0, n - 1
while rp > lp:
    cur = a[rp] + a[lp]
    if cur > m:
        rp -= 1
    elif cur <= m:
        c = max(cur, c)
        lp += 1
print(c)