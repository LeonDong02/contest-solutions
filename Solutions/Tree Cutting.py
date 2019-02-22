import sys
import heapq


def input():
    return sys.stdin.readline().strip()


def dijk(start, end):
    dist = [[[999999, 0] for _ in range(c)] for _ in range(r)]
    dist[start[1]][start[2]][0] = 0
    h = [start]
    while h:
        cur = heapq.heappop(h)
        for i in range(4):
            q = [cur[1] + mud[i], cur[2] + mlr[i]]
            if (0 <= q[0] < r) and (0 <= q[1] < c):
                if dist[q[0]][q[1]][0] > cur[0] + grid[q[0]][q[1]]:
                    dist[q[0]][q[1]][0] = cur[0] + grid[q[0]][q[1]]
                    if grid[q[0]][q[1]]:
                        dist[q[0]][q[1]][1] = dist[cur[1]][cur[2]][1] + 1
                    else:
                        dist[q[0]][q[1]][1] = dist[cur[1]][cur[2]][1]
                    heapq.heappush(h, [dist[q[0]][q[1]][0], q[0], q[1]])
    return dist[end[0]][end[1]][1]


mud = [0, 0, 1, -1]
mlr = [1, -1, 0, 0]
r, c = map(int, input().split())
grid = [[] for _ in range(r)]
tall = 0
dest = []
for i in range(r):
    cur = input().split()
    for j in range(c):
        if cur[j] not in '.X':
            grid[i].append(int(cur[j]))
            if int(cur[j]) > tall:
                tall = int(cur[j])
                dest = [[i, j]]
            elif int(cur[j]) == tall:
                dest += [[i, j]]
        elif cur[j] == '.':
            grid[i].append(0)
        elif cur[j] == 'X':
            start = [0, i, j]
            grid[i].append(0)
mintall = [0, 0, 9999999]
for i in dest:
    cur = (i[0] - start[1])**2 + (i[1] - start[2])**2
    if cur < mintall[2]:
        mintall[0] = i[0]
        mintall[1] = i[1]
        mintall[2] = cur
print(dijk(start, mintall) - 1)
