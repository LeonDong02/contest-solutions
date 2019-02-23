import sys
input = sys.stdin.readline


def func(arr):
    return a*arr[0] + b*arr[1] + c*arr[2]


n = int(input())
a, b, c = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(n)]
print(max(func(score[i]) for i in range(n)))
