# 백준 1932 https://www.acmicpc.net/problem/1932
N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

# 각 위치에서 합이 최대가 되는 경로를 저장할 dp
dp = []
for i in range(1, N+1):
    dp.append([0]*i)
dp[0][0] = triangle[0][0]


# 왼쪽 대각선 초기화
for i in range(1, N):
    dp[i][0] = dp[i-1][0]+triangle[i][0]

# 오른쪽 대각선 초기화
for i in range(1, N):
    last_index = len(dp[i])-1
    dp[i][last_index] = dp[i-1][last_index-1]+triangle[i][last_index]

# 안쪽에 있는 애를 훑는 dp[i][j]는 dp[i-1][j-1] dp[i-1]d[j] 둘 중 최대값과 기존 triangle[i][j]를 더함
for i in range(2, N):
    last_index = len(dp[i])-1
    for j in range(1, last_index):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[N-1]))
