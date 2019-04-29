import sys


def input():
    return sys.stdin.readline().strip()


n, m = map(int, input().split())
cap = list(map(int, input().split()))
stud = [[[0, i] for i in range(4)] for _ in range(n)]
for _ in range(m):
    cur = input().split()
    for i in range(n):
        stud[i][ord(cur[i]) - 65][0] += 1
for i in range(n):
    stud[i].sort(reverse=True)
    cur = [-1, -1]
    for j in range(4):
        if stud[i][j][0] < cur[0]:
            break
        if cap[stud[i][j][1]]:
            cur = stud[i][j]
    if cur[1] != -1:
        print(chr(cur[1] + 65))
        cap[cur[1]] -= 1
    else:
        print('E')
