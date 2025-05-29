#A01 모험가 길드
import time
N = int(input())
member = list(map(int, input().split()))
start_time = time.time()
#count1 = 0
count2 = 0
#i = 0

#member.sort(reverse=True)
#tmp = member[0]
#print(member)
#while True:
#    tmp = member[i]
#    i += tmp
#    if N < i + 1:
#        break
#    count1 += 1

i = 0
member.sort()
tmp = member[0]
while True:
    tmp = member[i]
    i += tmp
    if N < i + 1:
        break
    count2 += 1
print(count2)
#if(count1>count2):
#    print(count1)
#else:
#    print(coun...