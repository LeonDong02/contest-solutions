import sys
from bisect import bisect_right
input = sys.stdin.readline


n, k = map(int, input().split())
h = list(sorted(list(map(int, input().split()))))
c = 0
for i in range(n):
    c = max(c, bisect_right(h, h[i] + k) - i)
print(c)
