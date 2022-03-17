from collections import deque
n, m = map(int,input().split())
grid = []
result = 0
for i in range(n):
    grid.append(list(map(int,input().split())))
    
def meltingCheeze(delete_cheeze, grid):
    # 1. 인자로 받은 리스트에 해당하는 애들을 지움
    for location in delete_cheeze:
        grid[location[1]][location[0]] = 0
    return grid
dx = [1,0,-1,0]
dy = [0,1,0,-1]
delete_cheeze = []

while True:
    visited_area = [[-1]*m for _ in range(n)]
    queue = deque([[0,0]])
    visited_area[0][0]= 1
    # 0. 외부 공기는 3으로 채움 
    while queue:
        v = queue.popleft()
        grid[v[1]][v[0]] = 3
        for i in range(4):
            mx = v[0] + dx[i]
            my = v[1] + dy[i]
            if mx>=0 and my >=0 and mx <=m-1 and my<=n-1:
                if visited_area[my][mx] == -1 and grid[my][mx] != 1:
                    queue.append([mx,my])
                    visited_area[my][mx] = 1
    # 1. 지울 애들을 탐색하면서 찾음
    for y in range(1,n-1):
        for x in range(1,m-1):
            count = 0
            if grid[y][x] == 1:
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if grid[ny][nx] == 3:
                        count += 1
            if count >= 2:
                delete_cheeze.append([x,y])
                grid[y][x]=2
    if len(delete_cheeze) == 0:
        break
    # 2. 지울 애들을 담은 리스트를 멜팅치즈 함수로 보냄
    grid = meltingCheeze(delete_cheeze, grid)
    result += 1
    delete_cheeze = []
    

print(result)