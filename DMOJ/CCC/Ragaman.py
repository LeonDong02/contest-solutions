import sys


s1, s2 = list(input()), list(input())
s1.sort(reverse=True)
s2.sort(reverse=True)
for i in range(len(s1)):
    if s1[0] == s2[0]:
        s1.pop(0)
        s2.pop(0)
    elif s2[-1] == '*':
        s1.pop(0)
        s2.pop()
    else:
        print('N')
        sys.exit()
print('A')
