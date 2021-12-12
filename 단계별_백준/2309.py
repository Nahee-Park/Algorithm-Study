# 2309 일곱 난쟁이

from itertools import combinations

# 공백으로 분리된 입력은 몇번째 줄까지 있는지 주어줄 수 밖에 없다!
all = [int(input()) for _ in range(9)]
combination_items = list(combinations(all, 7))
result = 0

for item in combination_items:
    sum = 0
    for i in item:
        sum += i
    if sum == 100 :
        result = item
        break;

result = sorted(list(result))

for i in result:
    print(i)
