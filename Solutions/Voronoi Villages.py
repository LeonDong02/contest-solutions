num = int(input())
juxta = [int(input()) for i in range(num)]
juxta.sort()
min = ((juxta[1] - juxta[0]) / 2) + ((juxta[2] - juxta[1]) / 2)
for i in range(num - 2):
    if min > ((juxta[i+1] - juxta[i]) / 2) + ((juxta[i + 2] - juxta[i + 1]) / 2):
        min = ((juxta[i+1] - juxta[i]) / 2) + ((juxta[i + 2] - juxta[i + 1]) / 2)
print(min)