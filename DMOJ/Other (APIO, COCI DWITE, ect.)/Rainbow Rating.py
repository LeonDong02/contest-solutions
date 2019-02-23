import sys
input = sys.stdin.readline


n = int(input())
for _ in range(n):
    cur = int(input())
    if cur < 1000:
        print('Newbie')
    elif 1000 <= cur < 1200:
        print('Amateur')
    elif 1200 <= cur < 1500:
        print('Expert')
    elif 1500 <= cur < 1800:
        print('Candidate Master')
    elif 1800 <= cur < 2200:
        print('Master')
    elif 2200 <= cur < 3000:
        print('Grandmaster')
    elif 3000 <= cur < 4000:
        print('Target')
    elif 4000 <= cur:
        print('Rainbow Master')
