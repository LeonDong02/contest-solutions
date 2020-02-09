a, b, c, d, e, f = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
score1, score2 = (a * 3) + (b * 2) + c, (d * 3) + (e * 2) + f
if score1 > score2:
    print('A')
elif score2 > score1:
    print('B')
else:
    print('T')
