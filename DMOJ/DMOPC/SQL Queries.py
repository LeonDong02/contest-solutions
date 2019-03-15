import sys
cur = list(map(int, input().split()))
if 0 not in cur:
    print('NO')
    sys.exit()
else:
    for i in range(3):
        q = [i]
        while q[-1]:
            if cur[q[-1] - 1]:
                q.append(cur[q[-1] - 1])
            else:
                break
            if len(q) > 10:
                print('NO')
                sys.exit()
print('YES')
