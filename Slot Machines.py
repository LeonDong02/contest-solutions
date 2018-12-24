quarters = input()
machine1 = input()
machine2 = input()
machine3 = input()
counter1 = 35 - int(machine1)
counter2 = 100 - int(machine2)
counter3 = 10 - int(machine3)
count = 0
while int(quarters) > 0:
    counter1 -= 1
    quarters = int(quarters) - 1
    if int(counter1) == 0:
        quarters += 30
        counter1 += 35
    count += 1
    if int(quarters) == 0:
        break
    counter2 -= 1
    quarters = int(quarters) - 1
    if int(counter2) == 0:
        quarters += 60
        counter2 += 100
    count += 1
    if int(quarters) == 0:
        break
    counter3 -= 1
    quarters = int(quarters) - 1
    if int(counter3) == 0:
        quarters += 9
        counter3 += 10
    count += 1
print("Martha plays " + str(count) + " times before going broke.")
