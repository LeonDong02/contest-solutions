numbers = [float(input()) for i in range(int(input()))]
cup = 0
cdown = 0
for i in range(len(numbers)):
    if numbers[i] - int(numbers[i]) >= 0.5:
        cup += 1
    else:
        cdown += 1
print(cup)
print(cdown)
