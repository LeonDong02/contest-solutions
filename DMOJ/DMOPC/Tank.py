import sys
from bisect import bisect_right
input = sys.stdin.readline


n, p, m = map(int, input().split())
defense, resistance = [], []
for _ in range(n):
    u, v = map(int, input().split())
    defense.append(u)
    resistance.append(v)
phys = list(sorted(list(map(int, input().split()))))
mag = list(sorted(list(map(int, input().split()))))
prep, prem = [0], [0]
for i in range(p):
    prep.append(prep[-1] + phys[i])
for i in range(m):
    prem.append(prem[-1] + mag[i])
ind, val = 0, 99999999999999999
for i in range(n):
    curp, curm = bisect_right(phys, defense[i]), bisect_right(mag, resistance[i])
    cur = prep[-1] - prep[curp] + prem[-1] - prem[curm] - (p - curp)*defense[i] - (m - curm)*resistance[i]
    if cur < val:
        val = cur
        ind = i
print(ind + 1)
