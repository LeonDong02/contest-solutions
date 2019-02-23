encryp = list(input())
counter = 0
msg = input()
newmsg = ''
modval = 0
for j in str(msg):
    if j.isalpha():
        newmsg += j
final = ''
for i in str(newmsg):
    counter += 1
    modval = counter % len(encryp)
    if counter % len(encryp) == 0:
        modval = len(encryp)
    if ord(i) - 65 + ord(encryp[modval - 1]) > 90:
        final += chr(ord(i) - 91 + ord(encryp[modval - 1]))
    else:
        final += chr(ord(i) - 65 + ord(encryp[modval - 1]))
print(final)