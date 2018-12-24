a = input().split()
cities = [a[0]]
temp = [int(a[1])]
while cities[-1] != 'Waterloo':
    a = input().split()
    cities.append(a[0])
    temp.append(int(a[1]))

print(sorted(zip(cities, temp), key=lambda x: x[1])[0][0])
