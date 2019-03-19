import sys
from collections import deque
input = sys.stdin.readline


inf = 999999999999999


def solve():
    n = int(input())
    diameter = []
    mindia = inf
    for _ in range(n):
        cur = deque(list(map(int, input().split())))
        rid, r = cur.popleft(), cur.popleft()
        mincur = min(cur)
        if mincur < mindia:
            diameter = [rid]
            mindia = mincur
        elif mincur == mindia:
            diameter.append(rid)
    print(mindia, '{', end='')
    diameter.sort()
    for i in range(len(diameter) - 1):
        print(diameter[i], end=',')
    print(str(diameter[-1]) + '}')


for _ in range(10):
    solve()
