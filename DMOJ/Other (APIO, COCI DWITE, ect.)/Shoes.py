import sys


def input():
    return sys.stdin.readline().strip()


shoes = input().split()
left = []
right = []
for i in range(4):
    if shoes[i] == 'L':
        left.append(i + 1)
    else:
        right.append(i + 1)
for i in range(2):
    print(left[i], right[i])
