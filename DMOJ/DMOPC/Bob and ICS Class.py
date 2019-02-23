import math


rgb = [list(map(int, input().split())) for i in range(2)]
counter = 0
for i in range(2):
    for j in range(3):
        rgb[i][j] = int(math.sqrt(rgb[i][j]))
if rgb[0] == rgb[1]: print('Dull')
else: print('Colourful')
