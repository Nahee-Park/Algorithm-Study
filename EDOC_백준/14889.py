from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
mem = [i for i in range(N)]
combination_list = []

# 조합 이용해 가능한 팀 생성
for i in list(combinations(mem, N//2)):
    combination_list.append(i)

# 행렬 한 개 값이 100 넘지 않으므로 최대값 설정
min_gap = 100*N*N

for i in range(len(combination_list)//2):
    # A팀
    team = combination_list[i]
    A_ability = 0
    for j in range(N//2):
        mem = team[j]
        for k in team:
            A_ability += S[mem][k]  # 해당 멤버와 함께 할 때 능력치
    # B팀
    team = combination_list[-i-1]
    B_ability = 0
    for j in range(N//2):
        mem = team[j]
        for k in team:
            B_ability += S[mem][k]
    min_gap = min(min_gap, abs(A_ability-B_ability))

print(min_gap)


# 스타트팀의 능력치와 링크팀 능력치 차이가 최소
# 가능한 조합을 다 돌면서 리스트에 담고 그 조합등 중 차이가 최소인 두 조합을 찾기

# combination_list = list(combinations(S, N//2))


# for i in range(N):
#     for j in range(i+1, N):
#         # print(S[i][j])
#         # print(S[j][i])
#         ability_list.append(S[i][j]+S[j][i])

# # print(ability_list)
# ability_list = sorted(ability_list, reverse=True)
# combination_list = list(combinations(ability_list, N//2))


# for i in range(0, len(combination_list)):
#     sum_list.append(sum)
#     # print(sum)
#     sum = 0
#     for j in range(N//2):
#         sum += combination_list[i][j]
# # 합들의 리스트 ) 거기서 차가 최소인 것

# for i in range(len(sum_list)-1):
#     substract_list.append(abs(sum_list[i]-sum_list[i+1]))

# print("조합 리스트", combination_list)
# print("조합들 간의 합 리스트", sum_list)
# print("차 리스트", substract_list)
# # result = min(substract_list)
# # print(result)

# # for i in range(1, sum_list):
# #     # distract = 0
# #     for j in range(i+1, sum_list):
# #         sum_list[i]-sum_list[j]

# # for i in range(len(ability_list)-1):
# #     temp.append(abs(ability_list[i]-ability_list[i+1]))

# # print(temp)
# # result = min(temp)
# # print(result)
