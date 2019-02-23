import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
password = list(input())
dig, up, low, special = False, False, False, False
for i in password:
    if i in '1234567890':
        dig = True
    elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        up = True
    elif i in 'abcdefghijklmnopqrstuvwxyz':
        low = True
    elif i in '!@#$%^&*()-+':
        special = True
c = n
if not dig:
    c += 1
if not up:
    c += 1
if not low:
    c += 1
if not special:
    c += 1
print(max(6 - n, c - n))
