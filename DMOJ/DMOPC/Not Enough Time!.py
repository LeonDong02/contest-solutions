import sys
input = sys.stdin.readline


n, t = map(int, input().split())
dp = [0]*(t + 1)
for i in range(n):
    items = list(map(int, input().split()))
    for j in reversed(range(t + 1)):
        if j - items[0] >= 0:
            dp[j] = max(dp[j], dp[j - items[0]] + items[1])
        if j - items[2] >= 0:
            dp[j] = max(dp[j], dp[j - items[2]] + items[3])
        if j - items[4] >= 0:
            dp[j] = max(dp[j], dp[j - items[4]] + items[5])
print(dp[-1])
