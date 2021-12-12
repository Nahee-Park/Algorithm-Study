# 2460 지능형 기차

all = [list(map(int,input().split())) for _ in range(10)]
result = -1
sum = 0

for station in all:
    sum -= station[0]
    sum += station[1]
    if sum > result :
        result = sum
    
print(result)