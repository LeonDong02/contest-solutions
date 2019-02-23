import sys
input = sys.stdin.readline


n, m = map(int, input().split())
num = list(map(int, input().split()))
pre = [0]
for i in range(n):
    pre.append(pre[-1] + num[i])
lp, rp = 0, 1
maxi = 0
if sum(num) < m:
    print(n)
    sys.exit()
while rp < n:
    if pre[rp] - pre[lp] < m:
        if rp - lp > maxi:
            maxi = rp - lp
        rp += 1
    elif pre[rp] - pre[lp] >= m:
        lp += 1
print(maxi)
