order = input().split()
sortorder = sorted(order)
for i in range(5):
    for j in range(4-i):
        if order[j] > order[j+1]:
            temp = order[j]
            order[j] = order[j+1]
            order[j+1] = temp
            print(order[0] + " " + order[1] + " " + order[2] + " " + order[3] + " " + order[4])
