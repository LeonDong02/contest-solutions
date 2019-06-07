import sys


def input():
    return sys.stdin.readline().strip()


s, t = input(), input()
l = [0] * len(t)
i, c = 1, 0
while i < len(t):
    if t[i] == t[c]:
        c += 1
        l[i] = c
        i += 1
    else:
        if c:
            c = l[c - 1]
        else:
            l[i] = 0
            i += 1
i, j = 0, 0
while i < len(s):
    if t[j] == s[i]:
        i += 1
        j += 1
    if j == len(t):
        print(i - j)
        sys.exit()
    elif i < len(s) and t[j] != s[i]:
        if j:
            j = l[j - 1]
        else:
            i += 1
print(-1)