# 10818 최대, 최소 찾기 (라이브러리 사용하지 않고)

N = int (input())
nums = list(map(int,input().split()))
max_num = -1000000
min_num = 1000000

for num in nums:
    if max_num <= num :
        max_num = num
    if min_num >= num :
        min_num = num
        
print(min_num, max_num)
