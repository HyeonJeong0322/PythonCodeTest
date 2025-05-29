N, M = map(int, input().split())
big1= 0
for i in range(N):
    array = list(map(int, input().split()))
    array.sort()
    if big1 < array[0]:
        big1 = array[0]
print(big1)