import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(node):
    if node in leaves:
        cherry[node] = patch[node - 1]
        return cherry[node]
    else:
        cherry[node] = patch[node - 1] + sum(dfs(i[0]) for i in graph[node])
        for i in graph[node]:
            weight[i[0]] += i[1]
            weight[node] += weight[i[0]]
        return cherry[node]


n, c, k = map(int, input().split())
patch = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, kcur = map(int, input().split())
    graph[a].append([b, kcur])
cherry, weight = [0]*(n + 1), [0]*(n + 1)
leaves = []
for i in range(1, n + 1):
    if not len(graph[i]):
        leaves.append(i)
dfs(1)
count = 0
for i in range(2, n + 1):
    if cherry[i] >= c and weight[i] <= k:
        count += 1
print(count)
