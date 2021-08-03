# 13305 주유소 https://www.acmicpc.net/problem/13305
import sys
input = sys.stdin.readline

N = int(input())
road_length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
result = 0
# 첫번째 가격은 리스트 첫번째 항
now_price = oil_price[0]

for current_city in range(1, N):
    result += now_price * road_length[current_city-1]
    # 만약 새로운 오일 가격이 현재 오일 가격보다 싸면 지금 가격 바꿈
    if oil_price[current_city] < now_price:
        now_price = oil_price[current_city]

print(result)
