import sys
input = sys.stdin.readline


n = int(input())
h, e, p = [], [], []
for _ in range(n):
    hi, ei, pi = map(int, input().split())
    h.append(hi)
    e.append(ei)
    p.append(pi)
s = int(input())
dp = [0]*(s + 1)
c = [0]*(s + 1)
for i in range(n):
    for j in reversed(range(s + 1)):
        for k in range(1, s//p[i]):
            if j >= p[i]*k:
                if dp[j - p[i]*k] + h[i]*k - e[i]*k*(k - 1)//2 > dp[j]:
                    dp[j] = dp[j - p[i]*k] + h[i]*k - e[i]*k*(k - 1)//2
                    c[j] = c[j - p[i]*k] + k
                elif dp[j - p[i]*k] + h[i]*k - e[i]*k*(k - 1)//2 == dp[j]:
                    c[j] = min(c[j], c[j - p[i]*k] + k)
print(dp[-1])
print(c[-1])
