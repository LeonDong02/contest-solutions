def connected(start):
    global visited
    if start not in visited:
        visited.append(start)
        if graph[start]:
            for i in graph[start]:
                connected(i)


n, m, a, b = list(map(int, input().split()))
graph = {a: [], b: []}
visited = []
for i in range(m):
    x, y = map(int, input().split())
    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []
    graph[x].append(y)
    graph[y].append(x)
connected(a)
if b in visited:
    print('GO SHAHIR!')
else:
    print('NO SHAHIR!')
