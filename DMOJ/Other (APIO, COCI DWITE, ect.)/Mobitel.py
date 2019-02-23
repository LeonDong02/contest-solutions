order = input().split()
final = ''
same = [0 for i in range(8)]
for i in str(input()):
    if i in 'adgjmptw':
        counter = 1
    if i in 'behknqux':
        counter = 2
    if i in 'cfilorvy':
        counter = 3
    if i in 'sz':
        counter = 4
    if i in 'abc':
        if same[0] == 1:
            final += '#'
        final += (str(order.index('2') + 1) * counter)
        same = [0 for i in range(8)]
        same[0] = 1
    if i in 'def':
        if same[1] == 1:
            final += '#'
        final += (str(order.index('3') + 1) * counter)
        same = [0 for i in range(8)]
        same[1] = 1
    if i in 'ghi':
        if same[2] == 1:
            final += '#'
        final += (str(order.index('4') + 1) * counter)
        same = [0 for i in range(8)]
        same[2] = 1
    if i in 'jkl':
        if same[3] == 1:
            final += '#'
        final += (str(order.index('5') + 1) * counter)
        same = [0 for i in range(8)]
        same[3] = 1
    if i in 'mno':
        if same[4] == 1:
            final += '#'
        final += (str(order.index('6') + 1) * counter)
        same = [0 for i in range(8)]
        same[4] = 1
    if i in 'pqrs':
        if same[5] == 1:
            final += '#'
        final += (str(order.index('7') + 1) * counter)
        same = [0 for i in range(8)]
        same[5] = 1
    if i in 'tuv':
        if same[6] == 1:
            final += '#'
        final += (str(order.index('8') + 1) * counter)
        same = [0 for i in range(8)]
        same[6] = 1
    if i in 'wxyz':
        if same[7] == 1:
            final += '#'
        final += (str(order.index('9') + 1) * counter)
        same = [0 for i in range(8)]
        same[7] = 1
print(final)