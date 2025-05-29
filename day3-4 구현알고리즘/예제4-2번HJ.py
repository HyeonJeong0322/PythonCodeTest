#예제 4-2 시각

#3
#13
#23
#30 31 32 33 34 35 36 37 38 39
#43
#53
#15개.
#0~59 = 60개
#45 개 * 15
#15 개 * 60 
#시각이 3배수라면
#60 * 60

#for문 사용
#result = 45*15 + 15*60
#for i in range(1,N+1):
#    if(i == 3 or i == 13 or i == 23):
#        result += 60*60
#    else:
#        result += 45*15 + 15*60
#print(result)

#if문만 사용
N = int(input())
result = 0
if(N<3):
    result = (N+1)*(45*15 + 15*60)
elif(3<N<13):
    result = (N)*(45*15 + 15*60) + 60*60
elif(13<=N<23):
    result = (N-1)*(45*15 + 15*60) + 60*60*2
else:
    result = (N-2)*(45*15 + 15*60) + 60*60*3
    
print(result)