n = int(input())

arr = []

'''
# 리스트로 입력받기
for i in range(n):
    tmp = input().split()
    arr.append(tmp)
'''

# 튜플로 입력받기
for i in range(n):
    tmp = tuple(input().split())
    arr.append(tmp)

arr.sort(key=lambda x: int(x[1]))

for arr2 in arr:
    print(arr2[0], end=' ')