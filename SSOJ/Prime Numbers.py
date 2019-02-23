n, k = map(int, input().split())
primes = [True for i in range(n + 1)]
p = 2
c = 0
while p <= n:
    if primes[p]:
        if str(k) in str(p):
            c += p
        for i in range(p*2, n + 1, p):
            primes[i] = False
    p += 1
print(c)
