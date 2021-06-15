# 우선 정렬해서 각 요소의 숫자 셈 -> 1인 애들 몇명인지, 2인 애들 몇명인지, 3인 애들 몇명인지
# 공포도가 N에가까우면 우선 버리는 게 나음
# 해당 값보다 같거나 낮은 공포감을 가진 애들의 수를 세어봄 -> 그 값이 해당값보다 같거나 크면 그 값에 대한 조가 만들어질 수 있음

# 특정 공포도 f 보다 같거나 작은 공포도 값의 갯수 m
# f < m이면 나눠봄 . 그 몫만큼 조 만들 수 있음
# 그리고 빠진 애들은 N 값에서 빼줌
# f > m이면 못나눔. 그 공포도는 조 못만듦

from collections import Counter

# 입력 받음
N = int(input())
fear_array = list(map(int, input().split()))

# 정렬 후 각각 공포도별 수를 셈
fear_array = sorted(fear_array)
counter_fear = Counter(fear_array)
sum = 0
result = 0

for i in range(1, N+1):
    # 아직 팀 없는 애들의 숫자
    sum += counter_fear[i]
    if(sum <= counter_fear[i]):
        # 공포도i를 가진 애들 중 형성된 팀의 숫자
        team = 0
        team += sum // counter_fear[i]
        # 여기엔 팀의 수 누적
        result += team
        # 팀 생긴 애들은 빼줌
        sum -= team*i
    else:
        continue

print(result)
