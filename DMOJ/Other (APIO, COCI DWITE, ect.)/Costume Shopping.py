from collections import OrderedDict
input = __import__("sys").stdin.readline

n, m, q = map(int, input().split())
changes = [list(map(int, input().split())) for _ in range(q)]
minp = {changes[0][0]: changes[0][1]}
for i in range(1, q):
    if changes[i][0] not in minp:
        if changes[i][0] != changes[i - 1][0] + 1:
            minp[changes[i - 1][0] - 1] = changes[i - 1][1]
        minp[changes[i][0]] = min(changes[i][1], changes[i - 1][1])
    else:
        minp[changes[i][0]] = min(changes[i][1], minp[changes[i][0]])
if changes[-1][0] > 1:
    minp[changes[-1][0] - 1] = changes[-1][1]
days = [i for i in minp] + [0]
count = {1000000: n - changes[0][0]}
for i in range(len(days) - 1):
    if minp[days[i]] in count:
        count[minp[days[i]]] += days[i] - days[i + 1]
    else:
        count[minp[days[i]]] = days[i] - days[i + 1]
od = OrderedDict(sorted(count.items()))
c, t = 0, m
for i in od:
    if t >= od[i]:
        t -= od[i]
        c += od[i] * i
    else:
        c += i * t
        break
print(c)