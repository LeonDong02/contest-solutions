import sys
input = sys.stdin.readline


def fast_power(base, power):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base)
        power = power // 2
        base = (base * base)
    return result


def calc(deg, co, x):
    c = co[0]
    for i in range(1, deg + 1):
        c += co[i] * fast_power(x, i)
    return c


n = int(input())
f = list(reversed(list(map(int, input().split()))))
m = int(input())
g = list(reversed(list(map(int, input().split()))))
a, b = map(int, input().split())
mid = float(a + b) / 2
h = []
for i in xrange(min(n, m) + 1):
    h.append(f[i] - g[i])
if n > m:
    for i in xrange(m + 1, n + 1):
        h.append(f[i])
elif m > n:
    for i in xrange(n + 1, m + 1):
        h.append(-g[i])
deg = max(n, m)
cur = calc(deg, h, a)
f = 1
if cur > 0:
    f = 0
if not cur:
    print(a)
    sys.exit()
cur = calc(deg, h, b)
if not cur:
    print(b)
    sys.exit()
if f:
    while cur:
        cur = round(calc(deg, h, mid), 8)
        if cur > 0:
            b = mid
            mid = float(a + b) / 2
        elif cur < 0:
            a = mid
            mid = float(a + b) / 2
else:
    while cur:
        cur = round(calc(deg, h, mid), 8)
        if cur > 0:
            a = mid
            mid = float(a + b) / 2
        elif cur < 0:
            b = mid
            mid = float(a + b) / 2
sys.stdout.write(str(mid))
