n = int(input())
msg = list(input())
strmsg = ''.join(msg)
spe = []
c = 0
while c < len(msg):
    if msg[:c + 1] == msg[len(msg) - c - 1:]:
        spe.append(''.join(msg[:c + 1]))
    c += 1
c = 0
if ''.join(msg) not in spe:
    c += 1
for i in spe:
    for j in range(len(msg)):
        if ''.join(msg[j:j + len(i)]) == i:
            c += 1
print(c)
