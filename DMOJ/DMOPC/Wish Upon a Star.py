import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline


def dfs(c, p):
    visited[c] = True
    for i in graph[c]:
        if not visited[i]:
            if dfs(i, c):
                return True
        elif p != i:
            return True
    return False


c = False
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        if dfs(i, 0):
            if not c:
                c = True
            else:
                print('NO')
                sys.exit()
print('YES')
