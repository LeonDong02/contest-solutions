import sys


def input():
    return sys.stdin.readline().strip()


def solve():
    n = int(input())
    p = list(input())
    cur, path = '', ''
    s, e = 0, 0
    for i in range(2 * (n - 1)):
        if p[i] == 'S':
            s += 1
        elif p[i] == 'E':
            e += 1
        cur += p[i]
        if s == e:
            path += str(''.join(list(reversed(list(cur)))))
            cur = ''
    return path


for i in range(1, int(input()) + 1):
    print('Case #' + str(i) + ':', solve())
