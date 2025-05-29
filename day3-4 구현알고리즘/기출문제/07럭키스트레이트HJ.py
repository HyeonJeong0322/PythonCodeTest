gage = input()
left = 0
right = 0
for i in range (0,len(gage)):
    if i<len(gage)/2:
        left += int(gage[i])
    else:
        right += int(gage[i])
if left == right:
    print("LUCKY")
else:
    print("READY")
    