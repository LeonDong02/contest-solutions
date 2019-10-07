import sys
input = sys.stdin.readline


n = int(input())
a = [int(input())]
c = 1
cmax = a[0]
b = [a[0]]
for _ in range(n - 1):
    cur = int(input())
    a.append((cur + c) % 1000000000)
    if a[-1] >= cmax:
        cmax = a[-1]
        b.append(cmax)
        c += 1
    else:
        while b and b[-1] > a[-1]:
            b.pop()
            c -= 1
    print(c)
