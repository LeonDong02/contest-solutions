import sys
input = sys.stdin.readline


for _ in range(5):
    n = int(input())
    c = 0
    for i in range(2, n):
        while not n % i:
            n = n // i
            c += 1
    print(c)
