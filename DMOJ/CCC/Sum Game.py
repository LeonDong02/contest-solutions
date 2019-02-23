n = int(input())
t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))
c1, c2, cur = 0, 0, 0
for i in range(n):
    c1 += t1[i]
    c2 += t2[i]
    if c1 == c2:
        cur = i + 1
print(cur)
