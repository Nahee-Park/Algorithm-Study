
# 1448
import sys
input = sys.stdin.readline
N = int(input())
data = [int(input()) for _ in range(N)]
tri = []
# 삼각형이 되기 위한 조건 -> 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 한다.
data.sort(reverse=True)
for i in range(len(data)-2):
    if data[i] < data[i+1]+data[i+2]:
        tri.append(data[i]+data[i+1]+data[i+2])
    else:
        tri.append(-1)
print(max(tri))
