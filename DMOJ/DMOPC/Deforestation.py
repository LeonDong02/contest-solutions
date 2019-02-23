import sys


def input():
    return sys.stdin.readline().strip()


mass = [int(input()) for i in xrange(int(input()))]
presum = []
presum.append(mass[0])
for i in xrange(1, len(mass)):
    presum.append(presum[i - 1] + mass[i])
for i in xrange(int(input())):
    low, high = list(map(int, input().split()))
    print presum[high] - presum[low] + mass[low]
