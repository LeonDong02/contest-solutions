import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
c = [False, False]
for i in range(n):
    c[a[i] % 2] = True
    if c.count(True) == 2:
        break
if c.count(True) == 2:
    a.sort()
for i in range(n):
    print(a[i], end=' ')