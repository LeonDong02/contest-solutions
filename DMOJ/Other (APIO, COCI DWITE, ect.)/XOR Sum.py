import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
mina = [a[0]]
for i in range(1, n):
    if mina[-1] ^ a[i] <= mina[-1] + a[i]:
        mina[-1] ^= a[i]
    else:
        mina.append(a[i])
maxa = [a[0]]
for i in range(1, n):
    if maxa[-1] ^ a[i] >= maxa[-1] + a[i]:
        maxa[-1] ^= a[i]
    else:
        maxa.append(a[i])
print(sum(maxa) - sum(mina))
