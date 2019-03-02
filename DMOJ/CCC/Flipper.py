import sys


def input():
    return sys.stdin.readline().strip()


command = list(input())
grid = [1, 2, 3, 4]
if command.count('V') % 2 and command.count('H') % 2:
    grid = [4, 3, 2, 1]
elif command.count('V') % 2:
    grid = [2, 1, 4, 3]
elif command.count('H') % 2:
    grid = [3, 4, 1, 2]
print(grid[0], grid[1])
print(grid[2], grid[3])