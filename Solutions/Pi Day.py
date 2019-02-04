import sys
input = sys.stdin.readline


def pie(x, y):
    if x < 0:
        return 0
    if x == 0 or y == 1:
        dp[x][y] = 1
        return dp[x][y]
    if dp[x][y] > 0:
        return dp[x][y]
    dp[x][y] = pie(x, y - 1) + pie(x - y, y)
    return dp[x][y]


n, k = int(input()), int(input())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
print(pie(n - k, k))
