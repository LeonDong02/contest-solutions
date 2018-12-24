counter = 0
time = 1200
d = int(input())
counter += int(d / 720) * 31
d %= 720
for i in range(d):
    time += 1
    if time > 1259: time = 100
    elif time % 100 > 59: time += 40
    if time / 1000 > 1:
        if int(str(time)[1]) - int(str(time)[0]) == int(str(time)[2]) - int(str(time)[1]) == int(str(time)[3]) - int(str(time)[2]):
            counter += 1
    else:
        if int(str(time)[1]) - int(str(time)[0]) == int(str(time)[2]) - int(str(time)[1]):
            counter += 1
print(counter)