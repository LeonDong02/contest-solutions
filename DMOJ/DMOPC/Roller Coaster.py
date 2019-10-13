n, h1, h2 = map(int, input().split())
h = list(map(int, input().split()))
c = 0
for i in h:
    if h1 <= i <= h2:
        c += 1
print(c)