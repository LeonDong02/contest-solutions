def primes(prime, a, b, k):
    c = 0
    for i in range(a, b + 1):
        if prime[i] == k:
            c += 1
    return c


prime = [0 for i in range(10000001)]
p = 2
while p <= 10000000:
    if prime[p] == 0:
        for i in range(p, 10000001, p):
            prime[i] += 1
    p += 1

for i in range(int(input())):
    a, b, k = map(int, input().split())
    print('Case #' + str(i + 1) + ': ' + str(primes(prime, a, b, k)))
