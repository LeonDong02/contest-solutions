import sys
input = sys.stdin.readline


for _ in range(int(input())):
    h = int(input())
    cur = h // 3
    count = h - (cur * 3)
    if count == 0:
        print(cur * cur * cur)
    elif count == 1:
        print(cur * cur * (cur + 1))
    elif count == 2:
        print(cur * (cur + 1) * (cur + 1))
