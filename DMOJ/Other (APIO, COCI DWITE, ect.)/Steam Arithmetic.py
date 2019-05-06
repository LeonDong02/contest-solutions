import sys
from math import ceil


def input():
    return sys.stdin.readline().strip()


def div(a, b):
    return a // b if a // b >= 0 else ceil(a / b)


def solve():
    cur = list(''.join(input().split()))
    op, toeval = [], ''
    c = 0
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
                curop = op.pop()
                if curop != '//':
                    toeval += curop
                else:
                    toeval = list(toeval)
                    for j in reversed(range(len(toeval))):
                        if toeval[j] == '(' and not c:
                            toeval.insert(j, 'div')
                            break
                        elif toeval[j] == '(' and c:
                            c -= 1
                        elif toeval[j] == ')':
                            c += 1
                    toeval.append(', ')
                    toeval = ''.join(toeval)
    print(eval(toeval)) # eval is a FUNction


for _ in range(10):
    solve()

# finally fixed my code (so that one case wasn't hard coded)!
# use stacks to create an adjusted string with standard notation
# special div function because the division in this question is always absolute value floor (i.e negative number division is ceilinged)
