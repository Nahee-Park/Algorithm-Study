# https://www.acmicpc.net/problem/11048 이동하기
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

dp[0][0] = Map[0][0]

# 첫번째 행 초기화
for first_row in range(1, M):
    dp[0][first_row] = dp[0][first_row-1]+Map[0][first_row]

# 첫번째 열 초기화
for first_column in range(1, N):
    dp[first_column][0] = dp[first_column-1][0]+Map[first_column][0]

# 남은 애들은 이제 규칙에 따라 더할 거임
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + Map[i][j]

# print(dp)
print(dp[N-1][M-1])


# print(Map)

# # 0:오른쪽 한칸 1:아래로 한칸 2:대각선 아래로 한 칸
# dx = [1, 0, 1]
# dy = [0, 1, 1]

# direction = 0

# 일단 dp에 오른쪽 한 칸 왼쪽 한 칸 해서 한 면의 합을 구함
# 그 다음 행열에선 위와 왼쪽 중 최대값을 골라서 본인과 더해서 넣음
