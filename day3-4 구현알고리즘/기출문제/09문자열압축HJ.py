# s[j:j+1 for j in range(0,rlen(s),i)]
#arr = ['A','C','B']
#arr.sort()
#print(arr)
import textwrap
arr = input()
result = 0
i = 1
storelist = []
while i <= len(arr):
    countlist = textwrap.wrap(arr,i) # 자른 문자열 저장
    resultlist = []
    j = 0
    while j != len(countlist):
        countnum = 0
        if j == len(countlist) - 1:
            resultlist.append(countlist[j])
            break
        elif j == len(countlist):
            break
        while j + 1 < len(countlist):
            if countlist[j] == countlist[j+1]:
                    countnum+=1
                    j+=1
            else:
                break
        if 0 < countnum:
            resultlist.append(countnum+1)
            resultlist.append(countlist[j])
        else:
            resultlist.append(countlist[j])
        j += 1    
    
    storelist.append(''.join(map(str,resultlist)))
    
lencount = 1001
for k in range(0,len(storelist)):
    if lencount > len(storelist[k]):
        result = k
        lencount = len(storelist[k])

print(result)