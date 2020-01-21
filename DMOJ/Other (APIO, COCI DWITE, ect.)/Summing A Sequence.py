import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[0] = max(0, a[0]); dp[1] = max(0, a[1], dp[0])
for i in range(2, n):
    dp[i] = max(0, dp[i - 2] + max(0, a[i]), dp[i - 1])
print(dp[-1])
