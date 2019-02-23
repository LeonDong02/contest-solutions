import sys
import bisect


def input():
    return sys.stdin.readline().strip()


motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
a, b = int(input()), int(input())
for _ in range(int(input())):
    motels.append(int(input()))
motels.sort()
num_way = {i: 0 for i in motels}
num_way[0] = 1
for i in motels:
    if num_way[i] != 0:
        lo, hi = bisect.bisect_left(motels, i + a), bisect.bisect(motels, i + b)
        for j in range(lo, hi):
            num_way[motels[j]] += num_way[i]
print(num_way[7000])
