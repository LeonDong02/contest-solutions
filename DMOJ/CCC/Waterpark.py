import sys
input = sys.stdin.readline


n = int(input())
graph = []
for _ in range(n + 1):
    graph.append([])
x, y = map(int, input().split())
while x and y:
    graph[x].append(y)
    x, y = map(int, input().split())
dp = [0, 1] + [0]*(n - 1)
for i in range(1, n + 1):
    for j in graph[i]:
        dp[j] += dp[i]
print(dp[-1])
