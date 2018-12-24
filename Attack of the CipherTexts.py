a = input()
b = input()
c = input()
translatedstring = ''
counter = 0
for i in range(len(list(c))):
    for j in range(len(list(b))):
        if c[i] == b[j]:
            translatedstring = translatedstring + a[j]
            break
        elif j == len(list(b)) - 1:
            translatedstring = translatedstring + '.'
print(translatedstring)