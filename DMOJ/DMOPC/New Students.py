a = int(input())
total = sum(int(input()) for i in range(a))
for i in range(int(input())):
    total += int(input())
    print('{0:.3f}'.format(total/(a+i+1)))
