cities = ['Victoria', 'Edmonton', 'Winnipeg', 'Toronto', 'Halifax']
time = int(input())
print(time, 'in Ottawa')
time -= 300
if time < 0: time += 2400
for i in range(5):
    temp = time + (i * 100)
    if temp >= 2400: temp -= 2400
    print(temp, 'in', cities[i])
if temp + 30 >= 2400: temp -= 2400
if (temp + 30) % 100 > 59: temp += 40
print(temp + 30, "in St. John's")
