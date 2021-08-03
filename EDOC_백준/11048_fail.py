# https://www.acmicpc.net/problem/11048 이동하기
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# print(Map)

# 0:오른쪽 한칸 1:아래로 한칸 2:대각선 아래로 한 칸
dx = [1, 0, 1]
dy = [0, 1, 1]

direction = 0

# 초기 사탕 개수, 좌표 인덱스
candy = []
result_candy = Map[0][0]
mx = 0
my = 0

# 세 가지 케이스를 돌며 값을 비교해서 최대값을 고른 후 my_candy에 추가해서 출력
# 인덱스를 벗어나지 않도록 예외 처리
while True:
    # 인덱스 벗어나는 경우 나가기
    if my > N-2 or mx > M-2:
        print("반복문 나갈 때 mx, my", mx, my)
        break

    # 한 번 이동할 때 가능한 사탕 값 배열에 넣기
    for direction in range(3):
        candy.append(Map[my+dy[direction]][mx+dx[direction]])
        print("이런 사탕값이 들어왔엉!", candy)
    # 최대 사탕 값을 result_candy에 넣음
    result_candy += max(candy)
    # 최대값을 갖는 direction의 인덱스를 방향으로 설정
    direction = candy.index(max(candy))
    mx = mx+dx[direction]
    my = my+dy[direction]
    # 다음에 사탕들을 다시 담기 위해 리스트 초기화
    candy = []

print(result_candy)
