import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


n, q = map(int, input().split())
ratings = deque(list(map(int, input().split())))
presum = [0]
for _ in range(n):
    presum.append(presum[-1] + ratings.popleft())
for _ in range(q):
    a, b = map(int, input().split())
    print(presum[n] - presum[b] + presum[a - 1])
