import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


str = deque(input().split('dungeons and dragons'))
strc = len(str) - 1
for _ in range(len(str)):
    for i in str.popleft().split():
        str.append(i)
print((3*strc)/(len(str) + 3*(strc)))