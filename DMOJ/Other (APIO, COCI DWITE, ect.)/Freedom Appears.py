import sys
import math
from functools import reduce
input = sys.stdin.readline


x, y, z = map(int, input().split())
n = int(input())
vec = []
for i in range(n):
    a, b, c = map(int, input().split())
    cur = [x - a, y - b, z - c]
    div = abs(reduce(math.gcd, cur))
    for i in range(3):
        cur[i] /= div
    vec.append(str(cur))
print(len(set(vec)))
