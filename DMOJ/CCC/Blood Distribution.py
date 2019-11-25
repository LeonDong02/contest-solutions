import sys
input = sys.stdin.readline


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
for i in range(8):
    if b[i] <= a[i]:
        c += b[i]
        a[i] -= b[i]
        b[i] = 0
    else:
        c += a[i]
        b[i] -= a[i]
        a[i] = 0
        if i == 4 or i == 5:
            if not i % 2:
                x = 2
            else:
                x = 1
            for j in range(i - x, -1, -x):
                if j != 2 and j != 3:
                    if b[i] <= a[j]:
                        c += b[i]
                        a[j] -= b[i]
                        b[i] = 0
                    else:
                        c += a[j]
                        b[i] -= a[j]
                        a[j] = 0
        else:
            if not i % 2:
                x = 2
            else:
                x = 1
            for j in range(i - x, -1, -x):
                if b[i] <= a[j]:
                    c += b[i]
                    a[j] -= b[i]
                    b[i] = 0
                else:
                    c += a[j]
                    b[i] -= a[j]
                    a[j] = 0
print(c)
