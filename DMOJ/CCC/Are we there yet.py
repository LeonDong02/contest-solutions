distance = input().split()
distance.insert(0, 0)
total = []
total.append(int(distance[0]))
total.append(int(distance[0]) + int(distance[1]))
total.append(int(distance[0]) + int(distance[1]) + int(distance[2]))
total.append(int(distance[0]) + int(distance[1]) + int(distance[2]) + int(distance[3]))
total.append(int(distance[0]) + int(distance[1]) + int(distance[2]) + int(distance[3]) + int(distance[4]))
for i in range(5):
    final = ''
    for j in range(5):
        final += str(abs(total[i] - total[j])) + ' '
    print(final)