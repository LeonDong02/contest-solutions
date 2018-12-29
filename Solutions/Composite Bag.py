def isPrime(x):
    if x == 1:
        return False
    if all(x % i != 0 for i in range(2, int(x**(1/2)) + 1)):
        return True
    else:
        return False


bag = [int(input()) for i in range(int(input()))]
counter = 0
for i in range(len(bag)):
    if not isPrime(bag[i]):
        counter += 1
print(counter)
