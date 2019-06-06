import sys


def input():
    return sys.stdin.readline().strip()


def solve():
    n = int(input())
    num = list(map(int, list(input())))
    for i in range(n):
        if num[i] == 8 and n - i >= 11:
            return 'YES'
    return 'NO'


t = int(input())
for _ in range(t):
    print(solve())
    