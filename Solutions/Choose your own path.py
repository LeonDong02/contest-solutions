import math


def dijkstra(s, prev):
    global distance
    if math.isinf(distance[s - 1]):
        if distance[s - 1] > prev + 1:
            distance[s - 1] = prev + 1
        if graph[s]:
            for i in graph[s]:
                dijkstra(i, distance[s - 1])
    elif distance[s - 1] > prev + 1:
        distance[s - 1] = prev + 1


n = int(input())
end = []
distance = [math.inf for i in range(n)]
graph = {}
for i in range(1, n + 1):
    m = list(map(int, input().split()))
    graph[i] = []
    if m[0] == 0:
        end.append(i)
    for j in range(m[0]):
        graph[i].append(m[j + 1])
dijkstra(1, 0)
if all(not math.isinf(distance[i]) for i in range(n)):
    print('Y')
else:
    print('N')
print(min(distance[i - 1] for i in end))
