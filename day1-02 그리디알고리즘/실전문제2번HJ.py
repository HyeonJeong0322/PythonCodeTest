N, M, K = map(int,input().split())
list1 = list(map(int, input().split()))
count = 0
result = 0
big1=0
big2=0
for i in range(0,N):
    if list1[i] > big1:
        big2 = big1
        big1 = list1[i]
        
while True:
    if count >= M:
        break
    for i in range(0,K) :
        result += big1
        count += 1
    result += big2
    count +=1
print(result)
