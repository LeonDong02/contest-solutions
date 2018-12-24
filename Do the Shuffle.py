arr = ['A', 'B', 'C', 'D', 'E']
a, b = int(input()), int(input())
while a != 4:
    for i in range(b):
        if a == 1:
            arr.append(arr[0])
            del arr[0]
        if a == 2:
            arr.insert(0, arr.pop())
        if a == 3:
            arr[0], arr[1] = arr[1], arr[0]
    a, b = int(input()), int(input())
for i in range(5):
    print(arr[i], end=' ')
