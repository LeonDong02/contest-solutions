num = input()
j = 1
k = int(int(num)/2)
for i in range(1, (int(num)+1)):
    print(("*" * ((j*2)-1)) + (" " * (4*k)) + ("*" * ((j*2)-1)))
    if i > int(int(num)/2):
        j = j-1
        k = k+1
    else:
        j = j+1
        k = k-1