#A03 문자열 뒤집기
s = input()
nums = list(map(int, s))
count = 0
check = nums[0]
for i in range(len(nums)):
    if check != nums[i]:
        count += 1
        check = nums[i]

if count % 2 == 0:
    print(count // 2)
else:
    print(count // 2 + 1)
# 달라지는 횟수를 세서 count
# 짝수면 / 2, 홀수면 / 2 + 1