def coalition(votes):
    majority = sum(votes) // 2 + 1
    votesort = sorted(votes)
    c = 0
    while sum(votesort[n - 1 - c:]) < majority:
        c += 1
    return c + 1


n, d = map(int, input().split())
votes = list(map(int, input().split()))
changes = [list(map(int, input().split())) for i in range(d)]
print(coalition(votes))
for i in range(d):
    votes[changes[i][0] - 1] = changes[i][1]
    print(coalition(votes))
