a = int(input())
x = []
y = []
for i in range(a):
    point = input()
    temp = point.split()
    x.append(int(temp[0]))
    y.append(int(temp[1]))
x.sort()
y.sort()
if y[a-1] - y[0] >= x[a-1] - x[0]:
    print((y[a-1]-y[0])**2)
if x[a-1] - x[0] > y[a-1] - y[0]:
    print((x[a-1]-x[0])**2)
