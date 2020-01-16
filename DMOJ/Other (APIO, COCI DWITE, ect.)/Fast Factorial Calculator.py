import sys
input = sys.stdin.readline


mod = 1 << 32
for _ in range(int(input())):
    c = int(input())
    if c >= 40:
        print(0)
    else:
        ans = 1
        for i in range(2, c + 1):
            ans = (ans * i) % mod
        print(ans)
