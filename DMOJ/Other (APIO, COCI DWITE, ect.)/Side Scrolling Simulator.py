import sys


def input():
    return sys.stdin.readline().strip()


def solve():
    j, w, h = map(int, input().split())
    h -= 1
    j = min(j, h)
    plat = list(reversed([list(input()) for _ in range(h)]))
    sharp = input()
    start = plat[0].index('L')
    end = plat[0].index('G')
    lowop, lowbl = [-1] * w, [inf] * w
    for i in range(start, end + 1):
        for k in range(h):
            if plat[k][i] in 'GL.' and lowop[i] == -1:
                lowop[i] = k
            elif plat[k][i] in '@' and lowbl[i] == inf:
                lowbl[i] = k
    for i in range(start + 1, end):
        if lowop[i] > j or (lowop[i] > 0 and (lowop[i] >= lowbl[i - 1] or lowop[i] >= lowbl[i + 1])) or lowop[i] == -1:
            return i + 1
    return 'CLEAR'


inf = 9999999999999
for _ in range(10):
    print(solve())