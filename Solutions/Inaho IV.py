n = int(input())
coord = [list(map(float, input().split())) for i in range(2)]
distance = 0
for i in range(n):
    distance += (coord[0][i] - coord[1][i])**2
print(distance**(1/2))
