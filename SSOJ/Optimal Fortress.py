mx = 0
my = 0
l = 0
for i in range(int(input())):
    x, y, w, h = map(int, input().split())
    if w*h > l:
        l = w*h
        mx = x
        my = y
print(mx, my)