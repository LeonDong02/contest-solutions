import sys
input = sys.stdin.readline


primes = [True]*1000002
primes[0], primes[1] = False, False
p = 2
while p**2 <= 1000001:
    if primes[p]:
        for i in range(p*2, 1000002, p):
            primes[i] = False
    p += 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(primes[a:b].count(True))
