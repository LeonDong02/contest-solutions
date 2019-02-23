import sys


def input():
    return sys.stdin.readline().strip()


t = [0]*2001
s = [0]*4001
long, num = 0, 0
n = int(input())
for i in list(map(int, input().split())):
    t[i] += 1
for i in range(1, 2001):
    if t[i]:
        for j in range(i, 2001):
            if i == j:
                s[i + j] += t[i]//2
            elif t[j]:
                s[i + j] += min(t[i], t[j])
for i in range(1, 4001):
    if s[i] > long:
        long = s[i]
        num = 1
    elif s[i] == long:
        num += 1
print(long, num)
