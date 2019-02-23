def search(n, x, y):
    global c
    p = (x + y)//2
    if p == n:
        return c + 1
    if p > n:
        c += 1
        return search(n, x, p)
    else:
        c += 1
        return search(n, p, y)


n, x, y = map(int, input().split())
c = 0
print(search(n, x, y))
