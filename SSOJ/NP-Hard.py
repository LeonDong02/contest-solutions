n = int(input())
numbers = list(map(int, input().split()))
for i in range(n):
    print('yes' if numbers[i] > 20 else 'no')
