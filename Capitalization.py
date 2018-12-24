string = input().split()
if string[0][0] in 'abcdefghijklmnopqrstuvwxyz':
    string[0] = chr(ord(string[0][0]) - 32) + string[0][1:]
print(string[0], end=' ')
for i in range(1, len(string)):
    if '.' in string[i - 1] and string[i][0] in 'abcdefghijklmnopqrstuvwxyz':
        string[i] = chr(ord(string[i][0]) - 32) + string[i][1:]
    print(string[i], end=' ')
