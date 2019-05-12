import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    avg = sum(p) // n
    c = 0
    for i in range(n):
        c += abs(avg - p[i])
    print(c // 2)


for _ in range(5):
    solve()
