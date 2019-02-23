import sys
input = sys.stdin.readline


def fun(x, n):
    if n == 1:
        return 1
    return sum(fun(i, n - 1) for i in range(x + 1, b - n + 1))


n = int(input())
a, b = map(int, input().split())
a, b = 0, b - a + 1
print(fun(a, n - 2))