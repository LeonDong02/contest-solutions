n = int(input())
lot = [input() for i in range(2)]
counter = 0
for i in range(n):
    if lot[0][i] == lot[1][i] == 'C':
        counter += 1
print(counter)