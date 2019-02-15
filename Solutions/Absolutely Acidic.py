import sys
input = sys.stdin.readline


n = int(input())
c = [0 for _ in range(1001)]
for _ in range(n):
    c[int(input())] += 1
diflen = {}
for i in range(len(c)):
    if c[i] not in diflen:
        diflen[c[i]] = []
    diflen[c[i]].append(i)
if len(diflen[max(diflen)]) > 1:
    print(diflen[max(diflen)][-1] - diflen[max(diflen)][0])
    sys.exit()
cur = diflen[max(diflen)][0]
del diflen[max(diflen)]
print(max(diflen[max(diflen)][-1] - cur, cur - diflen[max(diflen)][0]))
