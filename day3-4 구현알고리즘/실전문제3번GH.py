n, m = map(int, input().split())
a, b, d = map(int, input().split())

arr1 = [[0]*m for _ in range(n)]
arr2 = [[0]*m for _ in range(n)]

for i in range(n):
    arr1[i] = list(map(int, input().split()))

#print(arr1)


da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
arr2[a][b]=1

cnt = 1
cnt_d = 0
while 1:
    nd=(d-1)%4
    na=a+da[nd]
    nb=b+db[nd]
    if arr1[na][nb]==0 and arr2[na][nb]==0:
        d=nd
        a=na
        b=nb
        cnt+=1
        arr2[a][b] = 1
        cnt_d=0
        continue
    else:
        d=nd
        cnt_d+=1

    if cnt_d==4:
        na=a-da[d]
        nb=b-db[d]
        if arr1[na][nb] == 1:
            break
        else:
            a=na
            b=nb
            cnt_d=0
            continue
    
print(cnt)
    
