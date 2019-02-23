import sys
import math
input = sys.stdin.readline


n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [abs(h[0] - h[i]) for i in range(k + 1)] + [math.inf]*(n - k - 1) if n > k else [abs(h[0] - h[i]) for i in range(n)]
for i in range(k + 1, n):
    dp[i] = min(dp[i - j] + abs(h[i] - h[i - j]) for j in range(1, k + 1))
print(dp[-1])
