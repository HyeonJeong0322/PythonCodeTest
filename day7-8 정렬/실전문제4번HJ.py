N, K = input().split()
Aarray = list(map(int,input().split()))
Barray = list(map(int,input().split()))

Aarray.sort()
Barray.sort(reverse= True)

for i in range(int(K)):
    if Aarray[i] < Barray[i]:
        Aarray[i] = Barray[i]

print(sum(Aarray))