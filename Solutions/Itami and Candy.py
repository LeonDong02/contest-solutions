n, x = map(int, input().split())


primes = [True for i in range(n + 1)]
p = 2
while p**2 <= n:
    for i in range(p*2, n + 1, p):
        primes[i] = False
    p += 1


counter = 0
for i in range(2, len(primes)):
    if primes[i]:
        if n - i < 0:
            break
        else:
            a = n - i
            counter += 2*(a//x)
            if a % x > 0:
                counter += 2
            else:
                counter += 1
print(counter)
