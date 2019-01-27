import sys
input = sys.stdin.readline


n, tasks = int(input()), list(map(int, input().split()))
dp = [True] + [False]*(sum(tasks)//2)
for i in range(n):
    for j in reversed(range(tasks[i], sum(tasks)//2 + 1)):
        if dp[j - tasks[i]]:
            dp[j] = True
for i in reversed(range(len(dp))):
    if dp[i]:
        print(sum(tasks) - 2*i)
        sys.exit()
