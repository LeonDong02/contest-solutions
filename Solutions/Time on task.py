import sys


def input():
    return sys.stdin.readline().strip()


t, c = int(input()), int(input())
chores = [int(input()) for i in range(c)]
chores.sort()
tot = 0
c = 0
while tot < t:
    tot += chores[c]
    c += 1
print(c if tot == t else c - 1)
