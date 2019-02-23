import sys


def input():
    return sys.stdin.readline().strip()


dist = int(input())
clubs = [int(input()) for i in range(int(input()))]
dp = [dist]*(dist + 1)
dp[0] = 0
for i in range(dist + 1):
    for j in clubs:
        if dp[0] != -1 and i + j <= dist:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
print('Roberta wins in ' + str(dp[-1]) + ' strokes.' if dp[-1] != dist else 'Roberta acknowledges defeat.')
