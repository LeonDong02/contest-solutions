import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
l, r = 0, 1
cur = 0
while r < n:
    if arr[r] - arr[l] <= 5:
        if cur < r - l:
            cur = r - l
        r += 1
    else:
        l += 1
print(cur + 1)
