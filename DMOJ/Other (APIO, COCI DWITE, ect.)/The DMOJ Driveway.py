import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


t, m = map(int, input().split())
q = deque([])
for _ in range(t):
    cur = input().split()
    if cur[1] == 'in':
        q.append(cur[0])
    else:
        if q[-1] == cur[0]:
            q.pop()
        elif q[0] == cur[0] and m:
            m -= 1
            q.popleft()
for i in q:
    print(i)