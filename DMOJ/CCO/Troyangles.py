import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
grid = [list(input()) for _ in range(n)]
dp = []
for i in range(n):
    dp.append([])
    for j in range(n):
        if grid[i][j] == '#':
            dp[i].append(1)
        else:
            dp[i].append(0)
for i in reversed(range(n - 1)):
    for j in range(1, n - 1):
        if grid[i][j] == '#':
            dp[i][j] += min(dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1])
print(sum(sum(dp[i]) for i in range(n)))