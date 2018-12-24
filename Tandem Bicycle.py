qNum = int(input())
n = int(input())
dmoj = list(map(int, input().split()))
peg = list(map(int, input().split()))
dmoj.sort()
if qNum == 1:
    peg.sort()
if qNum == 2:
    peg.sort(reverse=True)
print(sum(max(dmoj[i], peg[i]) for i in range(n)))
