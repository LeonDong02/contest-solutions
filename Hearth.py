n, t = map(int, input().split())
cardmana = [input().split() for i in range(int(n))]
cards = []
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if int(cardmana[i][1]) + int(cardmana[j][1]) + int(cardmana[k][1]) <= t:
                cards.append(sorted([cardmana[i][0], cardmana[j][0], cardmana[k][0]]))
cards.sort()
for a in cards:
    print(a[0], a[1], a[2])