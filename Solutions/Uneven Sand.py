import sys


current = 1000000000
upper = 2000000000
lower = 0
print(current)
a = input()
while a != 'OK':
    sys.stdout.flush()
    if a == 'SINKS':
        lower = current
        current = (current + upper) // 2
        print(current)
        a = input()
    if a == 'FLOATS':
        upper = current
        current = (current + lower) // 2
        print(current)
        a = input()
