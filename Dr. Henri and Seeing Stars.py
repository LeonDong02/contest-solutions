r, x, y = map(int, input().split())
stars = [list(map(int, input().split())) for i in range(3)]
stars.sort(key=lambda x: x[2])
if (x - stars[0][0])**2 + (y - stars[0][1])**2 < r**2:
    print('What a beauty!')
else:
    print('Time to move my telescope!')
