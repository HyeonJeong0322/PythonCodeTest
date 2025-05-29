#A04 만들 수 없는 금액
N = int(input())
coin = list(map(int, input().split()))
coin.sort()

if coin[0] > 1:
    print(1)
else:
    result = coin[0]
    
    for i in range(1,N):
        if coin[i-1] == coin[i] or coin[i-1] + 1 == coin[i] or result == coin[i] or result + 1 == coin[i]:
            result += coin[i]
        else:
            break
    print(result + 1)
# 입력한 리스트값을 오름차순으로 정렬하고
# 값이 점진적으로 커지거나,
# 이전숫자와 현재 숫자가 같거나,
# 현재까지 더한 값(또는 현재까지 더한 값 + 1) 이 현재 숫자 값이라면
# 현재 값을 누적해서 더한다.

# 11227 -> 14
# 11228 -> 7
# 3 3 7 8 21 -> 1
# 1 3 4 6 9 -> 2
# 1 2 3 7 14 -> 28
# 1 2 3 7 15 -> 14
