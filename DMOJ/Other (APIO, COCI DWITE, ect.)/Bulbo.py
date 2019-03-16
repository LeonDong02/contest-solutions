import sys
input = sys.stdin.readline


n, x = map(int, input().split())
ans = 0
lo, hi = x, x
for i in range(n):
    l, r = map(int, input().split())
    if l > hi:
        ans += l - hi
        lo, hi = hi, l
    elif r < lo:
        ans += lo - r
        hi, lo = lo, r
    else:
        lo, hi = max(lo, l), min(hi, r)
print(ans)
