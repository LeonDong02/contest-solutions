import sys
input = sys.stdin.readline


n = int(input())
a = list(sorted(list(map(int, input().split()))))
if sum(a[:n]) != sum(a[n:]):
    for i in a:
        print(i, end=' ')
else:
    print(-1)