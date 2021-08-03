from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())
students = [0] * n
data = [0] * 21
count = 0

for rank in range(n):
    name = len(stdin.readline().rstrip())  # 이름을 입력받음
    students[rank] = name  # 학생의 등수와 이름의 길이를 저장
    if rank > k:  # 만약 학생의 등수가 K보다 커지는 경우
        data[students[rank - k - 1]] -= 1  # 자신과 상관 없는 등수의 학생을 제거
    count += data[name]  # 자신과 이름의 길이가 같은 친구를 쌍으로 추가
    data[name] += 1  # 이름의 길이를 저장하는 리스트에 자신을 추가

print(count)
