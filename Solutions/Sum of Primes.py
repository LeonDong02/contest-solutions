def primes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p**2 <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    for p in range(2, n):
        if prime[p]:
            c += p
    return c


for i in range(5):
    print(primes(int(input())))
