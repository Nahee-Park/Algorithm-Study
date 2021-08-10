N, r, c = map(int, input().split())

# 일단 N값을 가지고 총 길이를 저장
length = (2 ** (N-1)*2 ** (N-1)) * 4
# r,c가 3,1로 주어진다면 이것은
# (r,c)가 몇번째 수인지 확인
row = int(length**(1/2))
coor = r*row+c+1
OD_list = []
result = 0
# 일단 length만큼의 1차원 배열을 만듦
for i in range(1, length+1):
    OD_list.append(i)

# 함수는 1차원 배열을 받아서 그 안에서 4개로 쪼개서 coor이 속하는 그룹을 찾는 방식


def division(OD_list, length, R, C):
    if(length > 0):
        # 일단 네 등분으로 자름
        a = OD_list[0:length//4]
        b = OD_list[length//4:length//2]
        c = OD_list[length//2:length//4*3]
        d = OD_list[length//4*3:]
        if coor in a:
            OD_list = a
        elif coor in b:
            OD_list = b
        elif coor in c:
            OD_list = c
        elif coor in d:
            OD_list = d
        length = length//4
        print(OD_list, length)
        division(OD_list, length)
    else:
        return
        # length를 4등분해서 그 안에 coor값이 들어가는지 보기


division(OD_list, length, 0, 0)

print(length)
print(coor)
