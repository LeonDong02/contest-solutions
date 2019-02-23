import sys
input = sys.stdin.readline


n, m, k = map(int, input().split())
blue, purple = 0, 0
for i in range(k):
    if n & (1 << i) and m & (1 << i):
        purple += 1
    elif n & (1 << i) or m & (1 << i):
        blue += 1
    else:
        purple += 1
print(blue, purple)
