N, K = map(int,input().split)
result = 1
count = 0
while True:
    if result > N:
        break
    result *= K
    count += 1
print(count)