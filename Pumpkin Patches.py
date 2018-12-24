coordx = []
coordy = []
for i in range(int(input())):
    temp = input().split()
    coordx.append(int(temp[0]))
    coordy.append(int(temp[1]))
coordx.sort()
coordy.sort()
print((coordx[-1] - coordx[0] + coordy[-1] - coordy[0]) * 2)
