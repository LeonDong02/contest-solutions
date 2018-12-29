n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
print(max(numbers, key=numbers.count))
