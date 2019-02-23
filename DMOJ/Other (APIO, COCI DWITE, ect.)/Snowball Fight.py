h1, w1 = map(int, input().split())
h2, w2 = map(int, input().split())
t1 = (h1 - 1)*w2
t2 = (h2 - 1)*w1
if t1 == t2:
    print(-1)
if t1 > t2:
    print(1)
if t1 < t2:
    print(2)
