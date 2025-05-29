#6번 무지 먹방
def solution(food_times, k):
    i = 0
    j = 0
    while True:
        if food_times.count(0) == len(food_times):
            return -1
        if food_times[i] == 0:
            i += 1
        food_times[i] -= 1
        if i == len(food_times) - 1:
            i = 0
        j += 1
        if k == j:
            break
    answer = i+1
    return answer