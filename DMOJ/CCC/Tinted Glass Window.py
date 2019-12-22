import sys
input = sys.stdin.readline

n, t = int(input()), int(input())
e, y = [], [] # e store events y store y values
for _ in range(n):
    cur = list(map(int, input().split()))
    e.append([cur[0], cur[1], cur[3], cur[4]]) #x, lo, hi, flag
    e.append([cur[2], cur[1], cur[3], -cur[4]]) # close event
    y.append(cur[1])
    y.append(cur[3])
e.sort(key=lambda x: x[0], reverse=True)
y = list(sorted(list(set(y)))) # list of y values for compression
coord = {}
for i in range(len(y)):
    coord[y[i]] = i # map compressed y coordinates
diff = [0] * len(y) # init difference array
tot, px = 0, 0 # total area, previous x value
while e:
    cx = e[-1][0]
    cur = [e.pop()] # list of events happening at current x value
    while e and e[-1][0] == cx:
        cur.append(e.pop()) # list of current events
    count = 0 if diff[0] < t else y[1] - y[0]
    a = [diff[0]]
    for i in range(1, len(diff)):
        a += [a[-1] + diff[i]]
        if a[i] >= t:
            count += y[i + 1] - y[i]
    tot += count * (cx - px)
    while cur:
        tcur = cur.pop()
        if tcur[-1] > 0:
            diff[coord[tcur[1]]] += tcur[-1]
            diff[coord[tcur[2]]] -= tcur[-1]
        elif tcur[-1] < 0:
            diff[coord[tcur[1]]] += tcur[-1]
            diff[coord[tcur[2]]] -= tcur[-1]
    if e:
        px = cx
sys.stdout.write(str(tot))
