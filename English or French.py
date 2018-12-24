countert = 0
counters = 0
for i in range(int(input())):
    for x in str(input()):
        if x in 't':
            countert += 1
        if x in 's':
            counters += 1
if countert > counters:
    print("English")
if countert == 0 and counters == 0:
    print("English")
elif counters >= countert:
    print("French")