import sys


def input():
    return sys.stdin.readline().strip()


n, t = map(int, input().split())
s = list(map(int, list(input())))
adv = 1
while t:
    cur = t & 1
    t >>= 1
    if cur:
        temp = [0] * n
        for i in range(n):
            temp[i] = s[(i - adv) % n] ^ s[(i + adv) % n]
        for i in range(n):
            s[i] = temp[i]
    adv <<= 1
for i in s:
    print(i, end='')