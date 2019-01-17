import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
h = list(map(int, input().split()))
dist = [0]*n
dist[1] = abs(h[1] - h[0])
for i in range(2, n):
    dist[i] = min(dist[i - 1] + abs(h[i] - h[i - 1]), dist[i - 2] + abs(h[i] - h[i - 2]))
print(dist[n - 1])
