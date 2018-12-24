sentence = input()
counter = 0
finalstring = ''
for i in range(len(sentence)):
    if counter == 0:
        finalstring += sentence[i]
        if sentence[i] in ['a', 'e', 'i', 'o', 'u']:
            counter += 2
    elif counter > 0:
        counter -= 1
print(finalstring)