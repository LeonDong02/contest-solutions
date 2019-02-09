import sys
import math
input = sys.stdin.readline


n = int(input())
tides = list(map(int, input().split()))
tides.sort()
low = tides[:math.ceil(n/2)]
high = tides[math.ceil(n/2):]
for i in range(n//2):
    print(low.pop(), high.pop(0), end=' ')
if low:
    print(low.pop())
