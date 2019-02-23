from collections import deque
import math


graph = {
    1: [6],
    2: [6],
    3: [4, 5, 6, 15],
    4: [3, 5, 6],
    5: [3, 4, 6],
    6: [1, 2, 3, 4, 5, 7],
    7: [6, 8],
    8: [7, 9],
    9: [8, 10, 12],
    10: [9, 11],
    11: [10, 12],
    12: [9, 11, 13],
    13: [12, 14, 15],
    14: [13],
    15: [3, 13],
    16: [17, 18],
    17: [16, 18],
    18: [16, 17]
}


z = input()
while z != 'q':
    x = int(input())
    if z == 'i':
        y = int(input())
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        if y not in graph[x]:
            graph[x].append(y)
            graph[y].append(x)
    elif z == 'd':
        y = int(input())
        if graph[x]:
            if y in graph[x]:
                del graph[x][graph[x].index(y)]
                del graph[y][graph[y].index(x)]
    elif z == 'n':
        print(len(graph[x]))
    elif z == 'f':
        level = [math.inf for i in range(50)]
        level[x] = 0
        q = deque([x])
        visited = [x]
        while q:
            a = q.popleft()
            for i in graph[a]:
                if i not in visited:
                    level[i] = level[a] + 1
                    q.append(i)
                    visited.append(i)
        print(level.count(2))
    elif z == 's':
        y = int(input())
        level = [math.inf for i in range(50)]
        level[x] = 0
        q = deque([x])
        visited = [x]
        while q:
            a = q.popleft()
            if graph[a]:
                for i in graph[a]:
                    if i not in visited:
                        level[i] = level[a] + 1
                        q.append(i)
                        visited.append(i)
        print(level[y] if not math.isinf(level[y]) else 'Not connected')
    z = input()
