import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = []
for _ in range(n + 1):
    graph.append([])
lengraph = [0]*(n + 1)
for _ in range(m):
    i, j = map(int, input().split())
    graph[j].append(i)
    lengraph[i] += 1
prob = [-1, 1/float(lengraph[1])] + [-1]*(n - 1)
for i in range(2, n + 1):
    prob[i] = sum(prob[j] for j in graph[i])
    if lengraph[i]:
        prob[i] /= lengraph[i]
for i in range(1, n + 1):
    if not lengraph[i]:
        print(prob[i])
