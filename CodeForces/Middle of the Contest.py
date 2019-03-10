import sys


def input():
    return sys.stdin.readline().strip()


t1h, t1m = map(int, input().split(':'))
t2h, t2m = map(int, input().split(':'))
dif = 0
if t1h > t2h:
    t1h -= 24
elif t1h == t2h and t1m > t2m:
    t1h -= 24
dif += (t2h - t1h)*60 + t2m - t1m
dif = dif//2
t1h += dif//60
t1m += dif % 60
if t1m > 59:
    t1m -= 60
    t1h += 1
while t1h < 0:
    t1h += 24
while t1h >= 24:
    t1h -= 24
t1h = list(str(t1h))
t1m = list(str(t1m))
while len(t1h) < 2:
    t1h = [0] + t1h
while len(t1m) < 2:
    t1m = [0] + t1m
print(str(t1h[0]) + str(t1h[1]) + ':' + str(t1m[0]) + str(t1m[1]))
