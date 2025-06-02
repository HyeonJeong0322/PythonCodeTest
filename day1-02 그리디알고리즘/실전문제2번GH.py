n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

num = k

arr.sort(reverse=True)

firstNum = arr[0]
secondNum = arr[1]
result = 0

for i in range(m):
    if num==0:
        result += secondNum
        num = k
    else:
        result += firstNum
        num-=1


print(result)