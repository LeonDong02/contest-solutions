def connected(x):
    global visited
    if x not in visited:
        visited.append(x)
        for i in graph[x]:
            connected(i)


visited = []
graph = {0: [], 1: [], 2: [], 3: []}
adj = [list(map(int, input().split())) for i in range(4)]
for i in range(4):
    for j in range(4):
        if i == j:
            pass
        elif adj[i][j] == 1:
            if j not in graph[i]:
                graph[i].append(j)
connected(0)
print('Yes' if sum(len(graph[i]) for i in range(4)) == 6 and all(i in visited for i in range(4)) else 'No')
