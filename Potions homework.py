students, tasks, times = list(), list(), list()
n = int(input())
for i in range(n):
    x = int(input())
    students.append(x)
    tasks.append(x)
students.sort()
tasks.sort()
for i in range(n):
    times.append(students[i] * tasks[n - 1 - i])
print(sum(times) % 10007)
