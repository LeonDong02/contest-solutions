import sys
input = sys.stdin.readline


n, k = map(int, input().split())
a = list(map(int, input().split()))
ind = [0] + [-1]*(k - 1)
c, cnt = -1, 0
for i in range(1, n + 1):
    cnt += a[i - 1]
    cnt %= k
    if ind[cnt] == -1:
        ind[cnt] = i
    else:
        c = max(c, i - ind[cnt])
print(c)