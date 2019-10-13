import sys
input = sys.stdin.readline


n = int(input())
a = list(sorted(list(map(int, input().split()))))
med = a[n // 2] if n % 2 else (a[n // 2] + a[n // 2 - 1]) / 2
a1 = a[:n // 2]
a2 = a[n // 2:] if not n % 2 else a[n // 2 + 1:]
med1 = a1[len(a1) // 2] if len(a1) % 2 else (a1[len(a1) // 2] + a1[len(a1) // 2 - 1]) / 2
med2 = a2[len(a2) // 2] if len(a2) % 2 else (a2[len(a2) // 2] + a2[len(a2) // 2 - 1]) / 2
print(a[0], a[-1], '{0:.6f}'.format(med1), '{0:.6f}'.format(med), '{0:.6f}'.format(med2))
