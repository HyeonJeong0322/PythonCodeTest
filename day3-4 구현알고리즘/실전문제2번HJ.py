#왕실의 나이트
N = input()
dx,dy = 0,0
#chr(97 == a)
#ord => 문자를 숫자화
dx = int(ord((N[0]))-96)
dy = int(N[1])
count = 0
if(dx - 1 > 0 and dy - 2 > 0):
    count += 1
if(dx - 2 > 0 and dy - 1 > 0):
    count += 1
if(dx - 2 > 0 and dy + 1 < 9):
    count += 1
if(dx - 1 > 0 and dy + 2 < 9):
    count += 1
if(dx + 1 < 9 and dy - 2 > 0):
    count += 1
if(dx + 2 < 9 and dy - 1 > 0):
    count += 1
if(dx + 2 < 9 and dy + 1 < 9):
    count += 1
if(dx + 1 < 9 and dy + 2 < 9):
    count += 1

print(count)

#h7 -> 7
#