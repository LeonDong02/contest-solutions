import sys
input = sys.stdin.readline


n = int(input())
sieve = [0] * (n + 1)
c = 1
for i in range(2, n + 1):
    if not sieve[i]:
        for j in range(i, n + 1, i):
            sieve[j] = c
        c += 1
for i in range(2, n + 1):
    print(sieve[i], end=' ')