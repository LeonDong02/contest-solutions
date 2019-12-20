import sys
input = sys.stdin.readline


n, k = map(int, input().split())
types = {}
for _ in range(n):
    c = int(input())
    if c not in types:
        types[c] = 0
    print(types[c])
    types[c] += 1
print(len(types))
