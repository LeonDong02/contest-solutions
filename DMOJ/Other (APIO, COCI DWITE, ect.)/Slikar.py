import sys


def input():
    return sys.stdin.readline().strip()


def solve(arr, s):
    if s == 1:
        c = 0
        for i in xrange(2):
            for j in xrange(2):
                c += arr[i][j]
        if c == 4:
            return [[1, 1], [1, 0]], 1, c
        if c == 0:
            return [[0, 0], [0, 1]], 1, c
        return arr, 0, c
    newsize, newsize2 = s >> 1, s << 1
    sa, ca, count1 = solve([arr[i][:s] for i in xrange(s)], newsize)
    sb, cb, count2 = solve([arr[i][s:newsize2] for i in xrange(s)], newsize)
    sc, cc, count3 = solve([arr[i][:s] for i in xrange(s, newsize2)], newsize)
    sd, cd, count4 = solve([arr[i][s:newsize2] for i in xrange(s, newsize2)], newsize)
    tosolve = [ca, cb, cc, cd]
    count = [count1, count2, count3, count4]
    ns = s * s
    countinv = [ns - count[i] for i in xrange(4)]
    config = [0] * 4
    mindiff = maxvalue
    for i in xrange(3):
        for j in xrange(i + 1, 4):
            cursum1 = tosolve[i] + tosolve[j]
            totest = []
            for k in xrange(4):
                if k != i and k != j:
                    totest.append(k)
            cursum2 = cursum1 + countinv[totest[0]] + count[totest[1]]
            cursum3 = cursum1 + countinv[totest[1]] + count[totest[0]]
            if cursum2 < mindiff:
                mindiff = cursum2
                config = [i, j, totest[0], totest[1]]
            if cursum3 < mindiff:
                mindiff = cursum3
                config = [i, j, totest[1], totest[0]]
    ans = [[], [], [], []]
    ans[config[2]] = [[1] * s for _ in xrange(s)]
    ans[config[3]] = [[0] * s for _ in xrange(s)]
    if not ans[0]:
        ans[0] = sa
    if not ans[1]:
        ans[1] = sb
    if not ans[2]:
        ans[2] = sc
    if not ans[3]:
        ans[3] = sd
    return [ans[0][i] + ans[1][i] for i in xrange(s)] + [ans[2][i] + ans[3][i] for i in xrange(s)], mindiff, sum(count[i] for i in xrange(4))


maxvalue = 10000000000000001
n = int(input())
g = [list(map(int, list(input()))) for _ in xrange(n)]
ans1, ans2, irrelevant = solve(g, n >> 1)
print(ans2)
for i in ans1:
    sys.stdout.write(''.join(list(map(str, i))) + '\n')
