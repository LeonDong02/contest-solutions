import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
code = list(input())
dna, rna = True, True
for i in range(n):
    if code[i] not in 'ACGTU':
        print('neither')
        sys.exit()
    if code[i] == 'T':
        rna = False
    elif code[i] == 'U':
        dna = False
if dna and rna:
    print('both')
elif dna:
    print('DNA')
elif rna:
    print('RNA')
else:
    print('neither')
