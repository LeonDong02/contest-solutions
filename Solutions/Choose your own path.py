from collections import deque


def connected(x):
    if x not in visited:
        visited.append(x)
        if graph[x]:
            for i in graph[x]:
                connected(i)


def distance(x):
    visited = [x]
    level = [1 for i in range(len(graph) + 1)]
    q = deque([x])
    while q:
        a = q.popleft()
        if graph[a]:
            for i in graph[a]:
                if i not in visited:
                    level[i] = level[a] + 1
                    q.append(i)
                    visited.append(i)
        else:
            return level[a]


n = int(input())
visited = []
graph = {}
for i in range(1, n + 1):
    m = list(map(int, input().split()))
    graph[i] = []
    for j in range(m[0]):
        graph[i].append(m[j + 1])
connected(1)
print('Y' if len(visited) == n else 'N')
print(distance(1))
