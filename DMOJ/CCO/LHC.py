import sys
input = sys.stdin.readline


def dfs(s, maxc, cnt):
    v[s] = True
    for i in graph[s]:
        if not v[i]:
            maxc, cnt = dfs(i, maxc, cnt)
            if dp[i] + dp[s] + 1 > maxc:
                maxc = dp[i] + dp[s] + 1
                cnt = c[i] * c[s]
            elif dp[i] + dp[s] + 1 == maxc:
                cnt += c[i] * c[s]
            if dp[i] + 1 > dp[s]:
                dp[s] = dp[i] + 1
                c[s] = c[i]
            elif dp[i] + 1 == dp[s]:
                c[s] += c[i]
    return maxc, cnt


n = int(input())
c = [1] * (n + 1)
v = [False] * (n + 1)
dp = [0] * (n + 1)
maxc, cnt = 0, 0
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
maxc, cnt = dfs(1, maxc, cnt)
print(maxc + 1, cnt)
