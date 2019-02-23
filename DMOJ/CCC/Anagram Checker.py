string = []
b = []
a = []
for i in range(2):
    a.append(input())
    string.append('')
    for x in str(a[i]):
        if x != ' ':
            string[i] += x
    b.append(''.join(sorted(string[i])))
if b[0] == b[1]:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
