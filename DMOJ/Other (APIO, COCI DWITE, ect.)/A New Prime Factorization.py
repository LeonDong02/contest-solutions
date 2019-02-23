def isPrime(x):
    if x == 1:
        return False
    if all(x % i != 0 for i in range(2, int(x**(1/2)))):
        return True
    else:
        return False


def printPrime(x):
    while x % 2 == 0:
        print(2)
        x /= 2
    for i in range(3, int(x**(1/2)), 2):
        while x % i == 0:
            print(i)
            x /= i
    if x != 1:
        print(int(x))


n = int(input())
if isPrime(n):
    print(n)
else:
    printPrime(n)
