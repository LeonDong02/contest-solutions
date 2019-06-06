import sys


def input():
    return sys.stdin.readline().strip()


r = []
val = [4, 8, 15, 16, 23, 42]
one = [True] * 6
for i in range(2, 6):
    print('?', 1, i)
    sys.stdout.flush()
    r.append(int(input()))
for i in range(4):
    for j in range(6):
        if r[i] % val[j]:
            one[j] = False
for i in range(4):
    for j in range(6):
        if one[j] and r[i] // val[j] not in val:
            one[j] = False
a = [val[one.index(True)]]
for i in range(4):
    a.append(r[i] // a[0])
for i in a:
    val.remove(i)
a.append(val[0])
print('!', a[0], a[1], a[2], a[3], a[4], a[5])