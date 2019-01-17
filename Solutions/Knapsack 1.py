import sys


def input():
    return sys.stdin.readline().strip()


c, m = map(int, input().split())
cages = [list(map(int, input().split())) for i in range(c)]
cost = [0]*(m + 1)
for i in range(1, c + 1):
    for j in reversed(range(cages[i - 1][0], m + 1)):
        cost[j] = max(cost[j], cages[i - 1][1] + cost[j - cages[i - 1][0]])
print(cost[m])
