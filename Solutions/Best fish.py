array1 = []
array2 = []
best1 = 0
best2 = 0
caught1 = input()
for x in range(0, int(caught1)):
    array1.append(0)
    array1[x] = input()
    measurements = array1[x].split()
    array1[x] = int(measurements[0]) * int(measurements[1])
    if x == 0:
        best1 = int(array1[x])
    else:
        if int(array1[x]) > best1:
            best1 = int(array1[x])
caught2 = input()
for y in range(0, int(caught2)):
    array2.append(0)
    array2[y] = input()
    measurements = array2[y].split()
    array2[y] = int(measurements[0]) * int(measurements[1])
    if y == 0:
        best2 = int(array2[y])
    else:
        if int(array2[y]) > best2:
            best2 = int(array2[y])
if best1 > best2:
    print("Casper")
elif best1 < best2:
    print("Natalie")
elif best1 == best2:
    print("Tie")