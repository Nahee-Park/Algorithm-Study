# 2210

# len측정 위해 문자열로 받음(int형은 len()이용 불가)
board = [list(map(str, input().split())) for _ in range(5)]

# 가능한 모든 경우의 여섯자리를 만든 뒤 set을 이용해 중복되는 것을 제외하고 그 set의 원소의 개수를 센다

# 동서남북 방향
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result_list = []


def dfs(x, y, number):
    global result_list
    if len(number) == 6:
        # result_list에 해당 숫자열이 없으면 추가
        if number not in result_list:
            result_list.append(number)
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >= 0 and nx < 5 and ny < 5:
            # number값을 갱신해서 6글자가 될 때까지 재귀
            dfs(nx, ny, board[nx][ny]+number)


# 모든 원소 돌면서 dfs함수 호출
for x in range(5):
    for y in range(5):
        # 전부 탐색, 첫 인덱스의 값을 일단 number로 보냄
        dfs(x, y, board[x][y])

result = len(result_list)
print(result)
