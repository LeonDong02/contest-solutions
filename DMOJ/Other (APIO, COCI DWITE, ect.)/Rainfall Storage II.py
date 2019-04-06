import sys
input = sys.stdin.readline


n = int(input())
h = list(map(int, input().split()))
pmax = [h[0]]
smax = [h[-1]]
for i in range(1, n):
    pmax.append(max(pmax[-1], h[i]))
for i in reversed(range(n - 1)):
    smax.append(max(smax[-1], h[i]))
smax = list(reversed(smax))
c = 0
for i in range(n):
    c += min(pmax[i], smax[i]) - h[i]
print(c)
