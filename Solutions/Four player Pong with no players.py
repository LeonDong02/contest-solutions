for i in range(5):
    h, v = int(input()), int(input())
    if v == 0:
        if h > 0:
            print('100,25')
        if h < 0:
            print('0,25')
    elif h == 0:
        if v > 0:
            print('50,50')
        if v < 0:
            print('50,0')
    else:
        r = min(abs(50/h), abs(25/v))
        print(str(int(50 + r*h)) + ',' + str(int(25 + r*v)))
