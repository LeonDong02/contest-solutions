import sys


def input():
    return sys.stdin.readline().strip()


n, t = map(int, input().split())
s = list(map(int, list(input())))
adv = 1
while t:
    if t & 1:
        temp = [s[(i - adv) % n] ^ s[(i + adv) % n] for i in range(n)]
        s = [temp[i] for i in range(n)]
    adv <<= 1; t >>= 1
print(''.join(list(map(str, s))))
