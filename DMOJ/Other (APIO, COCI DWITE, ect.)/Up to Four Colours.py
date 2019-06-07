import sys
from collections import deque
input = sys.stdin.readline


def bfs(x):
    q = deque([x])
    while q:
        cur = q.popleft()
        val = [False] * 5
        for i in graph[cur]:
            if not v[i]:
                q.append(i)
                v[i] = True
            val[c[i]] = True
        for i in range(1, 5):
            if not val[i]:
                c[cur] = i


for _ in range(5):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    v = [False] * (n + 1)
    c = [0] * (n + 1)
    for i in range(1, n + 1):
        if not v[i]:
            bfs(i)
    cur = len(list(set(c[1:])))
    print(cur if cur <= 4 else 0)
