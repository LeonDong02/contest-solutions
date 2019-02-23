import sys
input = sys.stdin.readline


def add(a):
    return (a*(a + 1))//2


n, m = map(int, input().split())
stab = [list(map(int, input().split())) for _ in range(m)]
stab.sort(key=lambda x: x[1])
i = 0
while i < len(stab) - 1:
    if (n - stab[i][0] + 1) - stab[i + 1][1] + stab[i][1] >= (n - stab[i + 1][0] + 1):
        del stab[i + 1]
    elif stab[i][1] == stab[i + 1][1]:
        del stab[i]
    else:
        i += 1
stab.append([0, n + 1])
c = 0
for i in range(len(stab) - 1):
    c += add(n - stab[i][0] + 1)
    if stab[i][1] + n - stab[i][0] + 1 >= stab[i + 1][1]:
        c -= add(n - stab[i][0] + 1 - stab[i + 1][1] + stab[i][1])
print(c)
