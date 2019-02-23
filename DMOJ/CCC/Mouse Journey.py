import sys


def input():
    return sys.stdin.readline().strip()


r, c = map(int, input().split())
cats = [list(map(int, input().split())) for _ in range(int(input()))]
grid = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
for i in range(1, r + 1):
    if [i, 1] in cats:
        break
    grid[i][1] = 1
for i in range(1, c + 1):
    if [1, i] in cats:
        break
    grid[1][i] = 1
for i in range(2, r + 1):
    for j in range(2, c + 1):
        if [i, j] not in cats:
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
print(grid[r][c])
