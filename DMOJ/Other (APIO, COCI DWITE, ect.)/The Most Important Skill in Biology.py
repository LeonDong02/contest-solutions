import sys
from math import ceil
input = sys.stdin.readline


n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
c = 0
for i in reversed(range(n)):
    c += points[i][0]*points[i - 1][1] - points[i][1]*points[i - 1][0]
print(ceil(abs(c/2)))
