import sys
input = sys.stdin.readline


n, c = map(int, input().split())
x, y = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
print(2*(max(y) - min(y) + max(x) - min(x))*c)
