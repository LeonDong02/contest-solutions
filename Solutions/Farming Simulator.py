n, m = list(map(int, input().split()))
farms = list(map(int, input().split()))
farms.sort()
counter = 0
for i in range(m, n):
    counter += farms[i]
print(counter)
