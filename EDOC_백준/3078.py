import sys
input = sys.stdin.readline

N, K = map(int, input().split())
name_len = [len(input().rstrip()) for _ in range(N)]  # 이름의 길이만 리스트에 담는다.
count = 0
# 이름의 길이를 인덱스로 친구 저장
data = [0] * 21

print(name_len)
for i in range(N):
    # 학생의 등수가 K보다 커지면 친구될 수 없는 등수 학생 제거
    if i > K:
        data[name_len[i-K-1]] -= 1
    # 제거하고 남은 애들 중에 이름의 길이가 같은 친구를 count
    count += data[name_len[i]]
    # 이름의 길이 저장하는 리스트에 자기 추가
    data[name_len[i]] += 1
    print(data)
print(count)
