def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if all(x % i != 0 for i in range(2, x)):
        return True
    else:
        return False


def secondPrimeDown(x):
    counter = 0
    secondPrime = 0
    while secondPrime < 2:
        x -= 1
        counter += 1
        if isPrime(x):
            secondPrime += 1
    return counter


def secondPrimeUp(x):
    counter = 0
    secondPrime = 0
    while secondPrime < 2:
        x += 1
        counter += 1
        if isPrime(x):
            secondPrime += 1
    return counter


def secondPrime(x):
    if secondPrimeDown(x) >= secondPrimeUp(x):
        return x + secondPrimeUp(x)
    elif secondPrimeDown(x) < secondPrimeUp(x):
        return x - secondPrimeDown(x)


for i in range(5):
    print(secondPrime(int(input())))
