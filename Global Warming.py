def findPattern(arr, n):
    newarr = []
    if arr.count(arr[0]) == len(arr) + 1:
        return 1
    newarr.append(arr.pop(0))
    while arr:
        if arr[0] == newarr[0]:
            if len(newarr) > len(arr):
                if newarr[:len(arr)] == arr:
                    return len(newarr)
            if all(newarr == arr[i*len(newarr):(i+1)*len(newarr)] for i in range(n//len(newarr) - 1)) and newarr[:(len(arr)%len(newarr))] == arr[:(len(arr)%len(newarr))]:
                return len(newarr)
        newarr.append(arr.pop(0))
    return n


arr = list(map(int, input().split()))
n = arr.pop(0)
while n:
    if n == 1:
        print(0)
        arr = list(map(int, input().split()))
        n = arr.pop(0)
    else:
        diffs = [arr[i] - arr[i + 1] for i in range(n - 1)]
        print(findPattern(diffs, n - 1))
        arr = list(map(int, input().split()))
        n = arr.pop(0)
