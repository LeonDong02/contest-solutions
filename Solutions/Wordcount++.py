import re

for i in range(5):
    counter = 0
    words = re.split("[' ]", input())
    for j in range(len(words)):
        count = 0
        for k in (words[j]):
            if k.isalpha():
                count += 1
        if count > 3:
            counter += 1
    print(counter)