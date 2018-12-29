import bisect


n, m = map(int, input().split())
lines = list(map(int, input().split()))
lines.sort()
while m:
    print(lines[0])
    bisect.insort(lines, lines.pop(0) + 1)
    m -= 1
