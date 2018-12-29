def isSquare(prime, x):
    if x**(1/2) - int(x**(1/2)) == 0 and prime[int(x**(1/2))] == 1:
        return True
    else:
        return False


prime = [0 for i in range(1001)]
p = 2
while p <= 1000:
    if prime[p] == 0:
        for i in range(p, 1001, p):
            prime[i] += 1
    p += 1

for i in range(5):
    a = int(input())
    if prime[a] == 2 or isSquare(prime, a):
        print('semiprime')
    else:
        print('not')
