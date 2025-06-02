n = int(input())
arr = [0]*n
for i in range (int(n)):
    arr[i] = int(input())

arr.sort(reverse=True)
print(arr)
