#A05 볼링공 고르기
from itertools import combinations
N, M = map(int,input().split())
data = list(map(int, input().split()))
result = len(list(combinations(data,2)))

for i in range(0, M):
    if data.count(i+1) > 1:
        result -= int(data.count(i+1)*(data.count(i+1)-1)/2)
print(result)