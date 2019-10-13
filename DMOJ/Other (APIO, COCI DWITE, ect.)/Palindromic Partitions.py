import sys


def input():
    return sys.stdin.readline().strip()


alph = {chr(i): i - 96 for i in range(97, 123)}
for _ in range(int(input())):
    s = input()
    a, b, c, p, power, l, r = 0, 0, 0, 29, 1, 0, len(s) - 1
    while r > l:
        a = (a + ((alph[s[l]] * power))) % 1000000007
        b = ((b * p) + alph[s[r]]) % 1000000007
        power *= p
        if a == b:
            a, b, power = 0, 0, 1
            c += 2
        l += 1
        r -= 1
    if l == r or a != b:
        c += 1
    print(c)