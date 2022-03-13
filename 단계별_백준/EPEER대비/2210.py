#  2210
board = [list(map(str,input().split())) for _ in range(5)]

dx = [0,1,-1,0]
dy = [1,0,0,-1]
result = set()

def dfs (x, y, num):
    # 길이가 6이되면 붙임
    if len(num) == 6:
        result.add(num)
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >=0 and nx< 5 and ny< 5:
            dfs(nx, ny, board[nx][ny]+num)

for x in range(5):
    for y in range(5):
        dfs(x,y, board[x][y])

print(len(result))