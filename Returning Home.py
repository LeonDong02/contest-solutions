q = []
q.append(input())
while q[-1] != 'SCHOOL':
    q.append(input())
q.pop()
while len(q):
    if len(q) == 1 and q[-1] == 'R':
        q.pop()
        print('Turn LEFT into your HOME.')
    elif len(q) == 1 and q[-1] == 'L':
        q.pop()
        print('Turn RIGHT into your HOME.')
    elif q[-1] == 'R':
        q.pop()
        print('Turn LEFT onto ' + q.pop() + ' street.')
    elif q[-1] == 'L':
        q.pop()
        print('Turn RIGHT onto ' + q.pop() + ' street.')
