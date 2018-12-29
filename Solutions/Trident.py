t = input()
s = input()
h = input()
for i in range(int(t)):
    print("*" + " " * int(s) + "*" + " " * int(s) + "*")
print("*" * 2 * int(s) + "*" * 3)
for j in range(int(h)):
    print(" " * int(((2 * int(s)) + 3) / 2) + "*")
