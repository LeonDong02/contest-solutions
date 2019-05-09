import sys


def input():
    return sys.stdin.readline().strip()


k, n = map(int, input().split())
word = [[] for _ in range(26)]
for _ in range(k):
    cur = input()
    word[ord(list(cur)[0]) - 97].append(cur)
for i in range(26):
    word[i].sort()
ind = [0 for _ in range(26)]
for _ in range(n):
    q = ord(input()) - 97
    print(word[q][ind[q]])
    ind[q] += 1
    if ind[q] == len(word[q]):
        ind[q] = 0
