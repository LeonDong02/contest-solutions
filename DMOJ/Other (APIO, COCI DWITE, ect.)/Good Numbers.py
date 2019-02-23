numbers = [int(input()) for i in range(int(input()))]
n = max(numbers)
prime = [True for i in range(n + 1)]
prime[0], prime[1] = False, False
p = 2
while p**2 <= n:
    if prime[p]:
        for i in range(p * 2, n + 1, p):
            prime[i] = False
    p += 1
c = 0
for i in range(len(numbers)):
    if prime[numbers[i]] and prime[sum(int(j) for j in str(numbers[i]))]:
        c += 1
print(c)
