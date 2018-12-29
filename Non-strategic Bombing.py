def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)


def inside(x1, y1, x2, y2, x3, y3, x, y):
    if area(x1, y1, x2, y2, x3, y3) == area(x, y, x2, y2, x3, y3) + area(x1, y1, x, y, x3, y3) + area(x1, y1, x2, y2, x, y):
        return True


n, m = map(int, input().split())
city = [list(map(int, input().split())) for i in range(n)]
plans = [list(map(int, input().split())) for i in range(m)]
for i in range(m):
    c = 0
    for j in range(n):
        if inside(plans[i][0], plans[i][1], plans[i][2], plans[i][3], plans[i][4], plans[i][5], city[j][0], city[j][1]):
            c += 1
    print(c)
