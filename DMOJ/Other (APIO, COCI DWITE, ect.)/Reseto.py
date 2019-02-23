n, k = map(int, input().split())
prime = [True for i in range(n + 1)]
p = 2
while p <= n:
    if prime[p]:
        for i in range(p, n + 1, p):
            if prime[i]:
                prime[i] = False
                current = i
            if prime.count(False) == k:
                break
    p += 1
    if prime.count(False) == k:
        break
print(current)
