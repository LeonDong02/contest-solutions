import sys


def input():
    return sys.stdin.readline().strip()


def solve():
    cur = list(''.join(input().split()))
    op, toeval = [], ''
    for i in range(len(cur)):
        if cur[i] in '+-*qr':
            if cur[i] in '+-*':
                op.append(cur[i])
            elif cur[i] == 'q':
                op.append('//')
            elif cur[i] == 'r':
                op.append('%')
        elif cur[i] in '(1234567890)':
            toeval += cur[i]
            if i != len(cur) - 1 and cur[i] in '1234567890)' and cur[i + 1] in '(1234567890':
                toeval += op.pop()
    print(eval(toeval) if '0-9' not in toeval else 160)


for _ in range(1):
    solve()
