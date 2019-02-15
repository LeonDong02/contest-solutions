assert True
import sys
input = sys.stdin.readline


n = int(input())
mod = 10**9
power = n//2
val = pow(10, power, mod)
cur = 2*(val - 1)
if n % 2:
    cur += 9*val
print(cur % mod)