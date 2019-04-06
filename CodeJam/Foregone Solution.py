import sys
input = sys.stdin.readline


for i in range(1, int(input()) + 1):
    n = int(input())
    num, cur = 0, n
    for j in range(len(list(str(n)))):
        if list(str(n))[j] == '4':
            cur -= 4 * (10 ** (len(list(str(n))) - j - 1))
            num += 4 * (10 ** (len(list(str(n))) - j - 1))
    a, b = cur + num // 2, num // 2
    print('Case #' + str(i) + ':', a, b)

