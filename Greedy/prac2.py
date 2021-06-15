# <첫번째 시도>
# 1. 0이 아니면 곱하는 게 무조건 이득
# 2. 0이면 더해야 함


S = list(map(int, input()))
count = 0
result = 0

for i in S:
    # 새로운 값이 0이면 우선 더함
    if(i == 0):
        if(count == 0):
            result = 0
        result += i
        count += 1
    # 새로운 값이 0이 아니면 검사
    else:
        # 만약 여태껏 값이 0이면 더하기
        if(result != 0):
            result *= i
            count += 1
        # 이전값, 이후값이 모두 0이 아니면 곱하기
        else:
            result += i
            count += 1

print(result)

# 이 코드의 문제점 -> 난잡함 + 1일 때도 더하는 게 최적임을 간과
# 02034958675849984759
# 47405481984000
# time: 6.079673767089844e-05
