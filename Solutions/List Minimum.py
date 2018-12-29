numbers = [int(input()) for i in range(int(input()))]
numbers.sort()
for i in range(len(numbers)):
    print(numbers.pop(0))
