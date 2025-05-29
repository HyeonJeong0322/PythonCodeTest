import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(np.rot90(a, 1)) # 반시계 방향 90도 회전

print(np.rot90(a, 2)) # 180도 회전

print(np.rot90(a, 3)) # 시계 방향 90도(반시계 방향 270도) 회전

N, M = 3, 3
key =  [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock =  [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
result = 0
for i in range(1,5):
    key = (np.rot90(key,i)
    tmplock = lock

key의 오른쪽 아래 모서리부터 Lock의 왼쪽위 모서리를 비교하기 시작해서
한칸씩 오른쪽으로 가고 
key의 왼쪽 아래 모서리와 Lock의 오른쪽 위 모서리를 비교한다면
한칸 아래로 내려가서 비교하기 시작하고
    겹치는 경우가 있으면 다음으로 넘어가고
    겹치지 않으면 빈공간을 체움

만약 Lock의 빈공간을 다 채우면 탈출하고 열린다 출력력

이렇게 모든 rotation 비교가 끝나고도 안열리면
False 출력
    