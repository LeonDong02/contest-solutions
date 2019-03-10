import sys
import bisect
from math import ceil
input = sys.stdin.readline


n, k = map(int, input().split())
arr = [i % k for i in list(map(int, input().split()))]
arr.sort()
c = (bisect.bisect_right(arr, 0) - bisect.bisect_left(arr, 0))//2
if not k % 2:
    c += (bisect.bisect_right(arr, k//2) - bisect.bisect_left(arr, k//2))//2
c *= 2
for i in range(1, ceil(k/2)):
    c += min((bisect.bisect_right(arr, i) - bisect.bisect_left(arr, i)), (bisect.bisect_right(arr, k - i) - bisect.bisect_left(arr, k - i)))*2
print(c)
