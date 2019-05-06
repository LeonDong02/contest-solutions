import sys
input = sys.stdin.readline


n = int(input())
for i in range(n // 2):
    print(1 + i, n - i, end=' ')
if n % 2:
    print(n // 2 + 1)
