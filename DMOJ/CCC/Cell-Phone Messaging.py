words = []
words.append(input())
while words[-1] != 'halt':
    words.append(input())
words.pop()
for j in range(len(words)):
    time = 0
    counter = 0
    same = [0 for i in range(8)]
    for k in str(words[j]):
        if k in 'adgjmptw':
            time += 1
        if k in 'behknqux':
            time += 2
        if k in 'cfilorvy':
            time += 3
        if k in 'sz':
            time += 4
        if k in 'abc':
            if counter == 1:
                time += 2
            counter = 1
        if k in 'def':
            if counter == 2:
                time += 2
            counter = 2
        if k in 'ghi':
            if counter == 3:
                time += 2
            counter = 3
        if k in 'jkl':
            if counter == 4:
                time += 2
            counter = 4
        if k in 'mno':
            if counter == 5:
                time += 2
            counter = 5
        if k in 'pqrs':
            if counter == 6:
                time += 2
            counter = 6
        if k in 'tuv':
            if counter == 7:
                time += 2
            counter = 7
        if k in 'wxyz':
            if counter == 8:
                time += 2
            counter = 8
    print(time)