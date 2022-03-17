n = int(input())
k = int(input())
apple_location = []
board = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int,input().split())
    apple_location.append([x,y])
    board[x-1][y-1] = 1
    
l = int(input())
snake_time = []
snake_direction = []
for _ in range(l):
    time, direction = map(str,input().split())
    snake_time.append(int(time))
    snake_direction.append(direction)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
current_direction = 0
snake_location = [[0,0]]
time = 0

def getDirection(str, current_direction):
    if str=='D':
        current_direction+=1
        if current_direction>=4:
            current_direction=0
    elif str=='L':
        current_direction-=1
        if current_direction<0:
            current_direction=3
    return current_direction
while True:
    # 시간에 따라 방향 바꿈 -> 숫자 커지면 오른쪽회전, 숫자 작아지면 왼쪽 회전
    if time in snake_time:
        idx = snake_time.index(time)
        current_direction = getDirection(snake_direction[idx],current_direction)
    # 마지막 좌표를 중심으로 움직여야 하므로
    pop_location = snake_location[-1] 
    nx = pop_location[0] + dx[current_direction]
    ny = pop_location[1] + dy[current_direction]
    
    if nx >= n or ny >= n or nx < 0 or ny < 0:
        break
    if board[ny][nx] == 1:
        snake_location.append([nx,ny])
    elif board[ny][nx] == 0:
        snake_location.append([nx,ny])
        # 첫번째 요소 지우기
        if len(snake_location)!=0:
            board[snake_location[0][1]][snake_location[0][0]] = 0 
            del snake_location[0]
    elif board[ny][nx] == 2:
        break
    # 몸통도 한방에 이동 
    for list in snake_location:
        board[list[1]][list[0]] = 2
    time += 1

        
print(time+1)        
    
