code = [input() for i in range(int(input()))]
decode = [code[i].split() for i in range(len(code))]
msg = input()
fmsg = ''
start = 0
while start < len(msg):
    k = 0
    for i in range(len(code)):
        if msg.find(decode[i][1], start) == start:
            k = i
            break
    fmsg += decode[k][0]
    start += len(decode[k][1])
print(fmsg)
