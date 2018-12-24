n, m = map(int, input().split())
total = 0
counter = 0
pieces = 0
while int(total) < n:
    if int((n * pieces) / m) != (n * pieces) / m:
        counter += 1
    total += n / m
    pieces += 1
print(counter)