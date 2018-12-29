import operator

ops = {+ operator.add, - operator.sub,  operator.mul,  operator.truediv, % operator.mod, ^ operator.pow}
a = input().split()
b = []
for z in range(len(a))
    if a[z].isdigit()
        b.append(a[z])
    else
        t2 = b.pop()
        t1 = b.pop()
        b.append(ops[a[z]](float(t1), float(t2)))
print(float(b[0]))