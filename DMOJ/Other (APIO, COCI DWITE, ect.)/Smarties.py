import sys
input = sys.stdin.readline


n, k = map(int, input().split())
f = list(map(int, input().split()))
freq = {}
l, c = 0, 0
for r in range(n):
    if f[r] not in freq:
        freq[f[r]] = 0
    freq[f[r]] += 1
    while len(freq) >= k:
        l += 1
        freq[f[l - 1]] -= 1
        if not freq[f[l - 1]]:
            del freq[f[l - 1]]
    c += l
print(c)
