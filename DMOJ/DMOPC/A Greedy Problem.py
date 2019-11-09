input = __import__("sys").stdin.readline


n, t, q = map(int, input().split())
ti = list(map(int, input().split()))
dp = [1] + [0] * t
for i in range(n):
    for j in reversed(range(t)):
        if dp[j] > 0 and j + ti[i] <= t:
            dp[j + ti[i]] += dp[j]
for i in range(t + 1):
    dp[i] %= 1000000007
for _ in range(q):
    a, b, q = map(int, input().split())
    q -= ti[a - 1] + ti[b - 1]
    ndp = dp[:]
    for i in range(ti[a - 1], q + 1):
        ndp[i] -= ndp[i - ti[a - 1]]
    for i in range(ti[b - 1], q + 1):
        ndp[i] -= ndp[i - ti[b - 1]]
    c = 0
    for i in range(q + 1):
        c += ndp[i]
    print(c % 1000000007)
