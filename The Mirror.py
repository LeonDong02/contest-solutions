def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if all(x % i != 0 for i in range(2, x)):
        return True
    else:
        return False


for i in range(int(input())):
    counter = 0
    a, b = list(map(int, input().split()))
    for j in range(a, b):
        if isPrime(j):
            counter += 1
    print(counter)
