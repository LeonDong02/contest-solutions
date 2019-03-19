import sys


def input():
    return sys.stdin.readline().strip()


def solve():
    t, n = map(int, input().split())
    c = 0
    for _ in range(n):
        if input() == 'B':
            c += t
        if c:
            c -= 1
    print(c)


for _ in range(10):
    solve()
