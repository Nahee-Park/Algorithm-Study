# def solution(n, lost, reserve):
#     answer = n - len(lost)
#     sorted_lost = sorted(lost)
#     sorted_reserve = sorted(reserve)     
#     for person in sorted_lost:
#         if person in sorted_reserve:
#             answer += 1
#             sorted_reserve.remove(person)
#             sorted_lost.remove(person)
#     for person in sorted_lost:
#         if person-1 in sorted_reserve:
#             sorted_reserve.remove(person-1)
#             answer+=1
#             continue
#         elif person+1 in sorted_reserve:
#             sorted_reserve.remove(person+1)
#             answer+=1
#     return answer

# 2차 코드 너무 더럽 
# def solution(n, lost, reserve):
#     answer = n - len(lost)
#     doubleValue = []
#     for person in lost:
#         if person in reserve:
#             answer += 1
#             doubleValue.append(person)
#     for value in doubleValue:
#         lost.remove(value)
#         reserve.remove(value) 
#     lost = sorted(lost)
#     reserve = sorted(reserve)
#     for person in lost:
#         if person-1 in reserve:
#             reserve.remove(person-1)
#             answer+=1
#             continue
#         elif person+1 in reserve:
#             reserve.remove(person+1)
#             answer+=1
#     return answer

#  최종
def solution(n, lost, reserve):
    new_lost = sorted([l for l in lost if l not in reserve])
    new_reserve = sorted([r for r in reserve if r not in lost])
    answer = n - len(new_lost)
    for i in new_lost:
        if i - 1 in new_reserve:
            new_reserve.remove(i - 1)
            answer += 1
            continue
        elif i + 1 in new_reserve:
            new_reserve.remove(i + 1)
            answer += 1
    return answer 


print(solution(5, [5,3], [2, 4]))


