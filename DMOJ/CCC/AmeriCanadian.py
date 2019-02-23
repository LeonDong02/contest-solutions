words = []
words.append(input())
while words[-1] != 'quit!':
    words.append(input())
words.pop()
for i in range(len(words)):
    test = ''
    for j in str(words[i][-2:]):
        test += j
    if test == 'or' and len(words[i]) > 4 and words[i][-3] in 'bcdfghjklmnpqrstvwxz':
        words[i] = words[i][:-1] + 'ur'
    print(words[i])