import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
a, b = list(input()), list(input())
a = [True if i == 'F' else False for i in a]
b = [True if i == 'F' else False for i in b]
for i in range(n - 1):
    if a[i]:
        a[i] = not a[i]
        a[i + 1] = not a[i + 1]
    if b[i]:
        b[i] = not b[i]
        b[i + 1] = not b[i + 1]
if a[-1] == b[-1]:
    print('YES')
else:
    print('NO')
