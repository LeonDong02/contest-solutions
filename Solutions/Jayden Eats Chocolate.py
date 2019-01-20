import sys
input = sys.stdin.readline


n = int(input())
choc = list(map(int, input().split()))
dp = [0]*(n + 1)
w = [0]*(n + 1)
for i in range(min(choc), n + 1):
    for j in range(3):
        w[i] = w[i - choc[j]] + choc[j] if i - choc[j] >= 0 and w[i - choc[j]] + choc[j] > w[i] else w[i]
    if w[i] == i:
        for j in range(3):
            dp[i] = dp[i - choc[j]] + 1 if i - choc[j] >= 0 and dp[i - choc[j]] + 1 > dp[i] else dp[i]
print(dp[-1])
