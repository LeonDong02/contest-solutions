import sys
input = sys,stn


radius = int(input())
while radius != 0:
    c = radius
    for i in range(1, radius):
        c += int((radius**2 - i**2)**(1/2))
    print(4*c + 1)
    radius = int(input())
