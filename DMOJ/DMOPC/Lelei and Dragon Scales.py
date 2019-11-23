from sys import stdin, stdout, exit, setrecursionlimit
from math import ceil
input = stdin.readline


w, h, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
psa = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
psa[1][1] = grid[0][0]
for i in range(2, w + 1):
    psa[1][i] = psa[1][i - 1] + grid[0][i - 1]
for i in range(2, h + 1):
    psa[i][1] = psa[i - 1][1] + grid[i - 1][0]
for i in range(2, h + 1):
    for j in range(2, w + 1):
        psa[i][j] = psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + grid[i - 1][j - 1]
factor = []
for i in range(1, ceil(n ** (1 / 2)) + 1):
    cur = n // i
    factor.append([i, cur])
    if i != cur:
        factor.append([cur, i])
c = 0
for f in factor:
    x, y = f[0], f[1]
    for i in range(h - x + 1):
        for j in range(w - y + 1):
            c = max(c, psa[i + x][j + y] - psa[i][j + y] - psa[i + x][j] + psa[i][j])
stdout.write(str(c))
