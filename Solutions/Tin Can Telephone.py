import sys
import math
input = sys.stdin.readline


def slope(x1, y1, x2, y2):
    if x2 == x1:
        return math.inf
    return (y2 - y1) / (x2 - x1)


def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    slope1 = slope(x1, y1, x2, y2)
    slope2 = slope(x3, y3, x4, y4)
    if slope1 == slope2:
        return False
    if math.isinf(slope1):
        if max(min(y1, y2), min(y3, y4)) <= slope2*x1 + (y3 - slope2*x3) <= min(max(y1, y2), max(y3, y4)):
            return True
        return False
    if math.isinf(slope2):
        if max(min(y1, y2), min(y3, y4)) <= slope1*x3 + (y1 - slope1*x1) <= min(max(y1, y2), max(y3, y4)):
            return True
        return False
    if max(min(x1, x2), min(x3, x4)) <= ((y1 - slope1*x1) - (y3 - slope2*x3))/(slope2 - slope1) <= min(max(x1, x2), max(x3, x4)):
        return True
    return False


xr, yr, xj, yj = map(int, input().split())
c = 0
for _ in range(int(input())):
    done = False
    num = list(map(int, input().split()))
    for i in range(num[0] - 1):
        if intersect(xr, yr, xj, yj, num[1 + i*2], num[2 + i*2], num[3 + i*2], num[4 + i*2]):
            c += 1
            done = True
            break
    if not done:
        if intersect(xr, yr, xj, yj, num[1], num[2], num[-2], num[-1]):
            c += 1
print(c)
