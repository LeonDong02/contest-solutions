def luckynumber(x):
    total = 0
    while int(x) > 9:
        for k in str(x):
            total = int(total) + int(k)
        x = int(total)
        total = 0
    return x


a = input()
array = []
numbers = []
for i in range(0, int(a)):
    array.append(0)
    numbers.append(0)
    numbers[i] = input()
    array[i] = luckynumber(numbers[i])

for j in range(0, int(a)):
    print(array[j])
