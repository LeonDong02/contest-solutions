n, k = map(int, input().split())
msg = list(map(int, input().split()))
mod = [0 for i in range(k + 1)]
tot = 0
for i in range(n):
    tot += msg[i]
    mod[((tot % k) + k) % k] += 1
res = 0
for i in range(k):
    if mod[i] > 1:
        res += (mod[i] * (mod[i] - 1)) // 2
res += mod[0]
print(res)
