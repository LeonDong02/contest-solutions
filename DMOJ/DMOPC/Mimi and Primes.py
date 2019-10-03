import sys
input = sys.stdin.readline


def rec(li):
    c = li.pop()
    while li:
        c = gcd(c, li.pop())
    return c


def gcd(a, b):
    if not a: return b
    if not b: return a
    return gcd(b, a % b)


n = int(input())
a = list(map(int, input().split()))
c = rec(a)
for i in reversed(range(int(c ** (1 / 2)) + 2)):
    if i == 1:
        print(c if c != 1 else 'DNE')
        sys.exit()
    if not c % i:
        print(i)
        sys.exit()