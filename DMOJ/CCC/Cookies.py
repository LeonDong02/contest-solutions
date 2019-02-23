import sys
input = sys.stdin.readline


def dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)


n = int(input())
chips = [list(map(int, input().split())) for _ in range(n)]
d = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j != k != i:
                a = dist(chips[i][0], chips[i][1], chips[j][0], chips[j][1])
                b = dist(chips[j][0], chips[j][1], chips[k][0], chips[k][1])
                c = dist(chips[i][0], chips[i][1], chips[k][0], chips[k][1])
                s = (a + b + c)/2
                if not s or a**2 + b**2 - c**2 < 0 or b**2 - a**2 + c**2 < 0 or a**2 - b**2 + c**2 < 0:
                    x = max(0, a, b, c)
                else:
                    x = 2*(a*b*c/(4*(s*(s-a)*(s-b)*(s-c))**(1/2)))
                if x > d:
                    d = x
print(d)
