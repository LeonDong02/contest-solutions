y, x = map(int, input().split())
grid = [input().split() for i in range(y)]
for i in range(3):
    grid = list(zip(*grid[::-1]))
for i in range(x):
    toPrint = ''
    for j in str(grid[i]):
        if j in '-1234567890 ':
            toPrint += j
    print(toPrint)
