def closeVowel(x):
    min = 26
    for i in 'aeiou':
        if abs(ord(x) - ord(i)) < min:
            min = abs(ord(x) - ord(i))
            vowel = i
    return vowel


def nextConsonant(x):
    if x == 'z':
        return 'z'
    elif x in 'dhnt':
        return chr(ord(x) + 2)
    else:
        return chr(ord(x) + 1)


toPrint = ''
for i in input():
    toPrint += i
    if i in 'bcdfghjklmnpqrstvwxyz':
        toPrint += closeVowel(i)
        toPrint += nextConsonant(i)
print(toPrint)
