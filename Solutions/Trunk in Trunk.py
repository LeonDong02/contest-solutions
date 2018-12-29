a = input()
t1 = list(map(int, a.split()))
b = input()
t2 = list(map(int, b.split()))
t1.sort()
t2.sort()
if all(t2[i] >= t1[i] for i in range(0, 3)):
    print("Y")
else:
    print("N")