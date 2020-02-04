import sys
input = sys.stdin.readline


t, d, p = map(int, input().split())
c = 0
if t < -40:
    c += 1
if d >= 15:
    c += 1
if p > 50:
    c += 1
if c >= 2:
    print('YES')
else:
    print('NO')
