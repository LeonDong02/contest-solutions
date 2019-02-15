import sys


def input():
    return sys.stdin.readline().strip()


n, m = map(int, input().split())
names = [input() for _ in range(n)]
votes = []
for _ in range(m):
    cur = input().split()
    votes.append([cur[i] for i in range(1, int(cur[0]) + 1)])
while len(names) > 1:
    ind = {names[i]: 0 for i in range(len(names))}
    for i in range(m):
        while votes[i] and votes[i][0] not in names:
            del votes[i][0]
        if votes[i]:
            ind[votes[i][0]] += 1
    count = [ind[i] for i in names]
    del names[count.index(min(count))]
print(names[0])
