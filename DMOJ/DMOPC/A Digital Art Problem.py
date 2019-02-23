import sys


def input():
    return sys.stdin.readline().strip()


def multiply(rgb):
    for i in range(3):
        print(rgb[0][i]*rgb[1][i], end=' ')


def screen(rgb):
    for i in range(3):
        print(1 - (1 - rgb[0][i])*(1 - rgb[1][i]), end=' ')


type = input()
rgb = [list(map(float, input().split())) for _ in range(2)]
if type == 'Multiply':
    multiply(rgb)
    sys.exit()
if type == 'Screen':
    screen(rgb)
    sys.exit()
if type == 'Overlay':
    for i in range(3):
        if rgb[0][i] < 0.5:
            print(2 * rgb[0][i] * rgb[1][i], end=' ')
        else:
            print(1 - 2*(1 - rgb[0][i])*(1 - rgb[1][i]), end=' ')
