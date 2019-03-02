import sys
input = sys.stdin.readline


n = int(input())
num = [int(input()) for _ in range(n)]
p = 2
cur = max(num)*2
primes = [True]*(cur + 1)
while p <= cur:
    if primes[p]:
        for i in range(p*2, cur + 1, p):
            primes[i] = False
    p += 1
for i in num:
    for j in range(i):
        if primes[i - j] and primes[i + j]:
            print(i - j, i + j)
            break
