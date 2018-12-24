maxweight = int(input())
trnum = int(input())
weight = [int(input()) for i in range(trnum)]
tweight = 0

def shiftwindow(tweight, weight, maxweight, trnum):
    for i in range(4):
        tweight += weight[i]
        if tweight > maxweight:
            return i
    for i in range(4, trnum):
        tweight += weight[i] - weight[i-4]
        if tweight > maxweight:
            return i
    return trnum

print(shiftwindow(tweight, weight, maxweight, trnum))
