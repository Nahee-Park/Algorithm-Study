import sys
input = sys.stdin.readline


n, r, c = map(int, input().split())


def division(n, r, c, result):

    if n == 0:
        return result
    # 구역 저장할 변수
    coord = [0, 0]

    if 2**(n-1) <= c:  # 중간보다 오른쪽에 있으면
        coord[1] = 1
    if 2**(n-1) <= r:  # 중간보다 아래에 있으면
        coord[0] = 1

    # 구역에 따라 좌표 갱신 + result값 갱신 후 함수 재귀적 호출
    if coord == [0, 0]:
        return division(n-1, r, c, result)
    elif coord == [0, 1]:
        c -= 2**(n-1)
        result += 2**(2*n-2)
        return division(n-1, r, c, result)
    elif coord == [1, 0]:
        r -= 2**(n-1)
        result += 2**(2*n-2)*2
        return division(n-1, r, c, result)
    elif coord == [1, 1]:
        r -= 2**(n-1)
        c -= 2**(n-1)
        result += 2**(2*n-2)*3
        return division(n-1, r, c, result)


print(division(n, r, c, 0))
