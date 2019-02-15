import sys
from collections import deque
input = sys.stdin.readline


s = deque(list(input()))
i = 0
while i < len(s):
    if s[i] not in 'love':
        del s[i]
    else:
        i += 1
while s[0] != 'l':
    s.popleft()
while s[-1] != 'e':
    s.pop()
dp = [0]*(len(s))
ind = {i : [] for i in 'love'}
c = 0
for i in range(len(s)):
    ind[s[i]].append(i)
for i in range(len(s)):
    if s[i] == 'l':
        for j in ind['o']:
            if j > i:
                dp[j] += 1
    elif s[i] == 'o':
        for j in ind['v']:
            if j > i:
                dp[j] += dp[i]
    elif s[i] == 'v':
        for j in ind['e']:
            if j > i:
                c += dp[i]
print(c)