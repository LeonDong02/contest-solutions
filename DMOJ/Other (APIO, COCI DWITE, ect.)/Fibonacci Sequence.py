import sys


def input():
    return sys.stdin.readline().strip()


q = {}


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    if n in q:
        return q[n]
    if n % 2 == 0:
        x = n//2
        result = fibonacci(x)*(2*fibonacci(x + 1) - fibonacci(x))
    else:
        x = (n - 1) // 2
        result = fibonacci(x + 1)**2 + fibonacci(x)**2
    result %= 1000000007
    q[n] = result
    return result


print(fibonacci(int(input())))
