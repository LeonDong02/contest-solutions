n = int(input())
counter = 0
studentAnswers = [input() for i in range(n)]
correctAnswers = [input() for i in range(n)]
for i in range(n):
    if studentAnswers[i] == correctAnswers[i]:
        counter += 1
print(counter)
