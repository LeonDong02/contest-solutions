number, counter = int(input()), 0
for i in range(number + 1):
    for k in range(i, number + 1):
        counter += k
        counter += i
print(counter)