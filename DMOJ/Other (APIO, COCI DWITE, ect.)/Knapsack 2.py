import sys


def input():
    return sys.stdin.readline().strip()


n, w = map(int, input().split())
dp = {0: 0}
for _ in range(n):
    wi, vi = map(int, input().split())
    for i in reversed(sorted(dp)):
        tempw = dp[i] + wi
        tempv = i + vi
        if tempw <= w:
            if tempv in dp:
                if tempw < dp[tempv]:
                    dp[tempv] = tempw
            else:
                dp[tempv] = tempw
print(max(dp))
