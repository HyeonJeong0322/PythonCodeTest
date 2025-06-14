from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# append로 삽입, popleft로 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(2)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력