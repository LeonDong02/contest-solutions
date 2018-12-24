str = [input() for i in range(10)]
counter = [0 for i in range(5)]
for i in range(5):
    word = ''
    for j in str[2 * i]:
        word += j
        if word in str[(2 * i) + 1]: counter[i] += 1
        else: break
for i in range(5):
    print(counter[i])