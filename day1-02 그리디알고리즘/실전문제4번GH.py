import math

n, k = map(int, input().split())

a = n - (n%k)

cnt = (n%k) + math.log(a,k)

print(int(cnt))


'''
n, k = map(int, input().split())

cnt = 0

while 1:
    if n == 1: break
    elif n%k == 0:
        n=n/k
        cnt+=1
    else:
        n-=1
        cnt+=1


print(cnt)
'''



