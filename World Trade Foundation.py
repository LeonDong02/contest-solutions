counter = 0
n, k = list(map(int, input().split()))
coins = list(map(int, input().split()))
for i in reversed(range(n)):
    counter += int(k / coins[i])
    k %= coins[i]
    if k == 0:
        print(counter)
        break
if k != 0:
    print(-1)