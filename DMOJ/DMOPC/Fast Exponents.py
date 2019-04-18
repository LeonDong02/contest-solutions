import sys
input = sys.stdin.readline


for _ in range(int(input())):
    i = int(input())
    if not i & i - 1:
        print('T')
    else:
        print('F')
