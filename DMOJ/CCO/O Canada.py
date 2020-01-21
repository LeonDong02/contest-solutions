import sys


def input():
    return sys.stdin.readline().strip()


n, g = int(input()), int(input())
gt = {}
for _ in xrange(g):
    grid = [[True if i == 'R' else False for i in list(input())] for _ in range(n)]
    for i in xrange(n - 1):
        for j in xrange(n - 1):
            if not grid[i][j]:
                grid[i][j] = not grid[i][j]
                grid[i + 1][j] = not grid[i + 1][j]
                grid[i][j + 1] = not grid[i][j + 1]
                grid[i + 1][j + 1] = not grid[i + 1][j + 1]
    t = ''
    for i in xrange(n - 1):
        t += '1' if grid[n - 1][i] else '0'
        t += '1' if grid[i][n - 1] else '0'
    t += '1' if grid[n - 1][n - 1] else '0'
    t = int(t, 2)
    try:
        test = gt[t]
    except KeyError:
        gt[t] = 0
    gt[t] += 1
sys.stdout.write(str(sum((gt[i]*(gt[i] - 1)) >> 1 for i in gt)))
