N, M = map(int, input().split())
nx, ny, dr = map(int, input().split())
maplist = []
for i in range (0,N):
    maplist.append(list(map(int,input().split())))
print(maplist)

dx = [-1,0,1,0]
dy = [0,-1,0,1]
d1 = [3,0,1,2]
d2 = [2,3,0,1]
count = 0
visit = 1
maplist[nx][ny] = 2

while True:
    if maplist[nx+dx[d1[dr]]][ny+dy[d1[dr]]] == 0:
        dr = d1[dr]
        nx = nx+dx[dr]
        ny = ny+dy[dr]
        maplist[nx][ny] = 2
        count = 0
        visit += 1
        print(nx,ny)
    else:
        dr = d1[dr]
        count += 1
    if count == 4:
        if maplist[nx+dx[d2[dr]]][ny+dy[d2[dr]]] == 2:
            nx = nx+dx[d2[dr]]
            ny = ny+dy[d2[dr]]
            count = 0
        else:
            break
    continue
print(visit)
    