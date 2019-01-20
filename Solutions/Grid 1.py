import sys


def input():
    return sys.stdin.readline().strip()


h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
gridval = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
for i in range(1, h + 1):
    if grid[i - 1][0] == '#':
        break
    gridval[i][1] = 1
for i in range(1, w + 1):
    if grid[0][i - 1] == '#':
        break
    gridval[1][i] = 1
for i in range(2, h + 1):
    for j in range(2, w + 1):
        if grid[i - 1][j - 1] != '#':
            gridval[i][j] = (gridval[i - 1][j] + gridval[i][j - 1]) % 1000000007
print(gridval[h][w])
