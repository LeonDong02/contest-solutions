string = input()
if string.count('not') % 2 == 0:
    print(string.split()[-1])
else:
    if string.split()[-1] == 'True':
        print('False')
    else:
        print('True')
