from bisect import bisect


g, p = int(input()), int(input())
planes = [int(input()) for _ in range(p)]
gates = [i + 1 for i in range(g)]
c = 0
for i in range(p):
    if not bisect(gates, planes[i]):
        break
    else:
        del gates[bisect(gates, planes[i]) - 1]
        c += 1
print(c)