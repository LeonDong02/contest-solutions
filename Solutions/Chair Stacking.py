import sys
input = sys.stdin.readline


n = int(input())
x, y, chair = [], [], []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    chair.append([a, b])
x.sort()
y.sort()
meeting = [x[n//2], y[n//2]] if n%2 else [(x[n//2] + x[n//2 - 1])//2, (y[n//2] + y[n//2 - 1])//2]
print(sum(abs(chair[i][0] - meeting[0]) + abs(chair[i][1] - meeting[1]) for i in range(n)))
