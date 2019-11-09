import sys, bisect
input = sys.stdin.readline

n, w = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ainv = [w - i for i in a]
c = 0
for i in range(n - 1):
    if a[i] > ainv[i]:
        break
    c += bisect.bisect_right(a, ainv[i]) - i - 1
print(c)