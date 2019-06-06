import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    c = 0
    while n:
        c += n % k
        n -= n % k
        n = n // k
        c += 1
    print(c - 1)