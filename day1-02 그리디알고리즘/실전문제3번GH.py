n, m = map(int, input().split())

result = 0

for i in range(n):
    arr = list(map(int, input().split()))
    if result < min(arr):
        result = min(arr)

print(result)




