import sys
input = sys.stdin.readline


def tot(a):
    return (a*(a + 1))//2


a, b = map(int, input().split())
print(tot(b) - tot(a - 1))
