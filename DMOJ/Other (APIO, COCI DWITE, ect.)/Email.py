import sys

def input():
    return sys.stdin.readline().strip()


def solve():
    n = int(input())
    emails = [input().split('@') for _ in range(n)]
    newemail = []
    for i in range(n):
        emails[i][0] = ''.join((emails[i][0].split('+')[0]).split('.')).lower()
        emails[i][1] = emails[i][1].lower()
        newemail.append(''.join(emails[i]))
    print(len(list(set(newemail))))


for _ in range(10):
    solve()
