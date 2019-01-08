import sys


def input():
    return sys.stdin.readline().strip()


n = ''.join(input().split())
c, long = 0, 0
for i in list(n):
    if i == 'L':
        c += 1
    else:
        if c > long:
            long = c
        c = 0
if c > long:
    long = c
print(n.count('L'), long)
