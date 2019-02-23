import sys


def input():
    return sys.stdin.readline().strip()


for _ in range(int(input())):
    string = list(input())
    dif = [abs(ord(string[i + 1]) - ord(string[i])) for i in range(len(string) - 1)]
    dif2 = [abs(ord(string[i]) - ord(string[i - 1])) for i in reversed(range(1, len(string)))]
    print('yes' if dif == dif2 else 'no')
