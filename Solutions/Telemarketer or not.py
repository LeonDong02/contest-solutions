digits = [int(input()) for i in range(4)]
if digits[0] > 7 and digits[3] > 7 and digits[1] == digits[2]:
    print('ignore')
else:
    print('answer')
