N = int(input())
tup = []
for _ in range(N):
    name, score = input().split()
    tup.append((name, int(score)))
sorttup = sorted(tup,key = lambda x:x[1])

#print(sorttup) 튜플 해당 값만 출력하는 방법
for i in sorttup:
    print(i[0], end=' ')