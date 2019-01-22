import sys
input = sys.stdin.readline


n, t = map(int, input().split())
coins = list(map(int, input().split()))
dp = [1] + [0]*t
for i in range(n):
    for j in reversed(range(coins[i], t + 1)):
        dp[j] += dp[j - coins[i]]
print(dp[-1])
