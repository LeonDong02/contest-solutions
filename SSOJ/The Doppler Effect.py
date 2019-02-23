for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > y:
        print('away')
    elif x < y:
        print('towards')
    elif x == y:
        print('none')
