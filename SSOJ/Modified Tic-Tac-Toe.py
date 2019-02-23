import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
grid = [list(input()) for _ in range(n)]
joon, shon = 0, 0
for i in range(n):
    if all(grid[i][j] == 'X' for j in range(n)):
        joon += 1
    elif all(grid[i][j] == 'O' for j in range(n)):
        shon += 1
    if all(grid[j][i] == 'X' for j in range(n)):
        joon += 1
    elif all(grid[j][i] == 'O' for j in range(n)):
        shon += 1
print(joon, shon)
if shon > joon:
    print('Shon')
elif joon > shon:
    print('Joon')
elif joon == shon:
    print('Tie')
