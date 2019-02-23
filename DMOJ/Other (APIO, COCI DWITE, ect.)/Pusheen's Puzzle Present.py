import sys
import math
input = sys.stdin.readline


n = int(input())
ok = False
grid = []
for _ in range(n):
    grid.append(input().split())
c = 0
for i in range(n):
    for j in range(n):
        if int(grid[i][j]) != i * n + j + 1:
            c += 1
print(math.ceil(c**(1/2)))
