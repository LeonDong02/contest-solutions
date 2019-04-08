import sys
input = sys.stdin.readline

a = [int(input()) for _ in range(9)]
c = False
for i in range(9):
    for j in range(9):
        if i != j and sum(a) - a[i] - a[j] == 100:
            a[i], a[j] = 0, 0
            c = True
            break
    if c: break
for i in range(9):
    if a[i]:
        print(a[i])
