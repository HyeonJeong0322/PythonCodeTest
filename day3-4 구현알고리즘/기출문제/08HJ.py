#arr = ['A','C','B']
#arr.sort()
#print(arr)
arr = []
numsum = 0
print(ord('9'),ord('A'))
#1 = 49 9 = 57 A = 56
instr = input()
for i in range(0,len(instr)):
    if 57 < ord(instr[i]):
        arr.append(instr[i])
    else:
        numsum += ord(instr[i]) - 48
arr.sort()
arr.append(str(numsum))
for i in range(0,len(arr)):
    print(arr[i], end="")
# list 문자열화 .join()
# print("".join(arr))