min = input()
max = input()
counter = 0


def test(x):
    total = ""
    for i in str(x):
        if int(i) == [2, 3, 4, 5, 7]:
            break
        if i == "6":
            total += "9"
        if i == "9":
            total += "6"
        if i == "1":
            total += "1"
        if i == "8":
            total += "8"
        if i == "0":
            total += "0"
    total = total[::-1]
    return total == str(x)


for i in range(int(min), int(max)):
    boolean = test(i)
    if boolean:
        counter += 1
print(counter)