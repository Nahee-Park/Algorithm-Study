import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dx = [0,1]
dy = [1,0]

def bfs():
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()

        if graph[x][y] == -1:
            return "HaruHaru"
        
        # 한번에 이동할 수 있는 거리 세팅
        distance = graph[x][y]

        for i in range(2):
            nx = x+ dx[i] * distance
            ny = y+dy[i] * distance

            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                visited[nx][ny] =1
                queue.append((nx,ny))
    return "Hing"

print(bfs())