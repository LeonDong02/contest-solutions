import sys
input = sys.stdin.readline


n = int(input())
c = 0
for _ in range(n):
    r, g, b = map(int, input().split())
    if 240 <= r <= 255 and 0 <= g <= 200 and 95 <= b <= 220:
        c += 1
print(c)
