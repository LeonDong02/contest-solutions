c, r = map(int, input().split())
a, b = map(int, input().split())
x, y = 0, 0
while not (a == 0 and b == 0):
    x += a
    y += b
    if x < 0:
        x = 0
    elif x > c:
        x = c
    if y < 0:
        y = 0
    elif y > r:
        y = r
    print(x, y)
    a, b = map(int, input().split())

