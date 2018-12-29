from bisect import bisect


g, p = int(input()), int(input())
planes = [int(input()) for i in range(p)]
gates = [i + 1 for i in range(g)]
counter = 0
for i in range(p):
    if bisect(gates, planes[i]) == 0:
        break
    else:
        del(gates[bisect(gates, planes[i]) - 1])
        counter += 1
print(counter)
