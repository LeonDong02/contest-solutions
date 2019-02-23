import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
x = [1 for i in range(n + 1)]
for i in range(1, n):
    a = int(input())
    x[a] *= 1 + x[i]
print(x[n])
