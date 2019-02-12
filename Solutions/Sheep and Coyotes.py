import sys
input = sys.stdin.readline


def distance(x1, y1, x2):
    return float(((x1 - x2)**2 + y1**2)**(1/2))


n = int(input())
sheepx, sheepy = [], []
xc = [False]*100001
lg = 0
for _ in range(n):
    x, y = float(input()), float(input())
    if xc[int(x*100)]:
        cur = sheepx.index(x)
        if sheepy[cur] > y:
            sheepy[cur] = y
    else:
        sheepx.append(x)
        sheepy.append(y)
        xc[int(x*100)] = True
        if x*100 > lg:
            lg = x*100
eat = [False]*(len(sheepx))
for i in range(100001):
    if xc[i] or i > lg:
        s = 9999
        ind = []
        for j in range(len(sheepx)):
            x = distance(sheepx[j], sheepy[j], i / 100)
            if x < s:
                ind = [j]
                s = x
            elif x == s:
                ind += [j]
        for j in ind:
            eat[j] = True
for i in range(len(sheepx)):
    if eat[i]:
        print('The sheep at (' + str("%.2f" % sheepx[i]) + ', ' + str("%.2f" % sheepy[i]) + ') might be eaten.')