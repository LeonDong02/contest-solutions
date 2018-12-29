def primes(largest, array):
    prime = [True for i in range(largest + 1)]
    prime[1] = False
    p = 2
    while p**2 <= largest:
        if prime[p]:
            for i in range(p * 2, largest + 1, p):
                prime[i] = False
        p += 1
    c = 0
    for i in range(len(array)):
        if prime[array[i]]:
            c += 1
    return c


n = int(input())
slices = list(map(int, input().split()))
slices.sort()
print(primes(slices[-1], slices))
