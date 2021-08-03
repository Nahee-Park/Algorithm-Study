# 13305 주유소 https://www.acmicpc.net/problem/13305
import sys
input = sys.stdin.readline

N = int(input())
road_length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

result = 0
cheap_index = 100000
expensive_index = 100000
current_city = 0

while True:
    for next_city in range(current_city+1, N):
        print("현재도시 오일 가격", oil_price[current_city])
        print("다음 도시 오일 가격", oil_price[next_city])
        # 오일 가격이 더 싼 애를 만나면 그 인덱스 중 최소값 저장
        if oil_price[current_city] > oil_price[next_city]:
            cheap_index = min(cheap_index, next_city)
        else:
            cheap_index = current_city
        # 오일 가격이 더 비싼 애를 만나면 그 인덱스 중 최소값 저장
        if oil_price[current_city] < oil_price[next_city]:
            expensive_index = min(expensive_index, next_city)
        else:
            expensive_index = current_city

    print(current_city, "번째 싼인덱스와 비싼인덱스", cheap_index, expensive_index)
    # 싼 곳 인덱스 < 비싼 곳 인덱스이면 일단 당장 갈 기름만 삼
    if cheap_index < expensive_index:
        result += oil_price[current_city] * road_length[current_city]
        current_city += 1
    # 비싼 곳 인덱스 < 싼 곳 인덱스이면 비싼 곳까지 가는 기름 다 삼
    elif cheap_index > expensive_index:
        # road[current_city] 부터 road[expensive_index]까지 다 현재 도시에서 사고 그 뒤의 싼 값을 새로운 인덱스로
        for i in range(current_city, expensive_index+1):
            result += oil_price[current_city]*road_length[i]
        current_city = cheap_index
    # 비싼 곳 인덱스와 싼 곳 인덱스가 같으면 현재가격으로 뒤에 애들 다 삼
    else:
        result += oil_price[current_city]*sum(road_length[current_city:])
        break

    # 인덱스 넘어가기 전에 예외 처리
    if current_city >= N-1 or expensive_index >= N-1:
        break

print(result)
