n = int(input())
orders = list(map(int, input().split()))
orders.sort()
num = []
for i in range(6):
    num.append(orders.count(i + 1))
print(num.index(max(num)) + 1)
print(num.index(min(num)) + 1)
