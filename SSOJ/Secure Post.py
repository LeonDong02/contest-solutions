import sys


def input():
    return sys.stdin.readline().strip()


letter = [chr(i + 97) for i in range(26)]
t = int(input())
for _ in range(t):
    n, string = input().split()
    string = list(string)
    for i in range(int(n)//2):
        string[i * 2], string[i * 2 + 1] = string[i * 2 + 1], string[i * 2]
    for i in range(int(n)):
        string[i] = letter[::-1][ord(string[i]) - 97]
        print(string[i], end='')
    print('')
