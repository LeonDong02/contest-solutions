import sys
input = sys.stdin.readline


n, m, a, b, c = map(int, input().split())
alien = list(map(int, input().split()))
y = list(map(int, input().split()))
for i in y:
    if alien[i - 1]:
        m += a
    else:
        m -= b
print(m)
