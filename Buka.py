import operator
ops = { "+": operator.add, "*": operator.mul }
val = []
for i in range(3):
    val.append(input())
print(ops[val[1]](int(val[0]), int(val[2])))
