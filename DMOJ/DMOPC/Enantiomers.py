import sys


def input():
    return sys.stdin.readline().strip()


mol1 = input().split()
mol2 = input().split()
c1, c2 = {}, {}
for i in range(4):
    if mol1[i] not in c1:
        c1[mol1[i]] = 0
    c1[mol1[i]] += 1
    if mol2[i] not in c2:
        c2[mol2[i]] = 0
    c2[mol2[i]] += 1
if c1 == c2:
    if mol1[0] == mol2[-1]:
        mol2 = mol2[::-1]
    if mol2[1] == mol1[0]:
        mol2 = [mol2[2], mol2[0], mol2[3]]
    elif mol2[2] == mol1[0]:
        mol2 = [mol2[0], mol2[1], mol2[3]]
    elif mol2[0] == mol1[0]:
        mol2 = [mol2[1], mol2[2], mol2[3]]
    mol1 = [mol1[1], mol1[2], mol1[3]]
    for i in range(3):
        if mol1 == [mol2[-i], mol2[1 - i], mol2[2 - i]]:
            print('NO')
            sys.exit()
    if mol2[-1] == mol1[0]:
        mol2 = mol2[::-1]
        mol2 = [mol2[2], mol2[1]]
    elif mol2[0] == mol1[0]:
        mol2 = [mol2[1], mol2[2]]
    elif mol2[1] == mol1[0]:
        mol2 = [mol2[2], mol2[0]]
    mol1 = [mol1[1], mol1[2]]
    if mol1[0] == mol2[1] and mol1[1] == mol2[0]:
        print('YES')
    else:
        print('NO')
else:
    print('NO')