array = []
total = 0
counter = 0
for i in range(int(input())):
    a = input()
    if int(a) > 0:
        array.append(a)
        counter += 1
    else:
        array.pop()
        counter -= 1
for j in range(int(counter)):
    total += int(array[j])
print(total)
