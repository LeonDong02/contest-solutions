import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
card = [int(input()) for i in range(n)]
dp = [0]*(n + 1)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + card[j - 1])
print(dp[-1])
