k = int(input())
x = float(input())
avg = []
for i in range(k):
    sequence = list(map(float, input().split()))
    avg.append(sum(sequence[1:]))
print(sum(avg)/k + x)
