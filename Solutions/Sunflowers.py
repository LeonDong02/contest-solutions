n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
didPrint = False
while not didPrint:
    if all(all(grid[i][j] > grid[i][j - 1] for j in range(1, n)) for i in range(n)) and all(all(grid[i][j] > grid[i - 1][j] for i in range(1, n)) for j in range(n)):
        for i in range(n):
            toPrint = ''
            for j in str(grid[i]):
                if j in '1234567890 ':
                    toPrint += j
            print(toPrint)
        didPrint = True
    else:
        grid = list(zip(*grid[::-1]))