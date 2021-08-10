# 일단 리스트로 입력 받고 각 숫자의 갯수를 카운터로 세서 dict에 넣음
# dict의 value 값이 3인 애를 일단 찾음
# dict의 value 값이 3인 애들의 인접한 key값을 찾음
# 그 key들의 value값을 찾기
# 그 value값들이 1,3,2인지 확인하고 True인 key를 찾기
from collections import Counter
num_list = [list(map(int, input().split())) for _ in range(12)]

# 입력받은 2차원 리스트를 1차원으로 변환 후 카운트해서 dict로 변환
od_list = sum(num_list, [])
counter = Counter(od_list)
num_dict = dict(counter)

# value값이 3인 key값을 저장한 리스트
candidate = [key for key, value in num_dict.items() if value == 3]
# print(candidate)

# candidate_item과 같은값이 있으면 그 연결값의 간선의 곱을 mul에 저장
# 그 곱이 6이면 (간선 1,3,2) 결과값에 그 간선을 가진 candidate_item값을 저장
result = 0

for candidate_item in candidate:
    mul = 1
    for item in num_list:
        if item[0] == candidate_item:
            mul *= num_dict[item[1]]
        elif item[1] == candidate_item:
            mul *= num_dict[item[0]]
    if mul == 6:
        result = candidate_item
        break


print(result)
