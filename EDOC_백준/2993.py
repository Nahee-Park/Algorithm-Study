# 2993
str = input()
n = len(str)
li = []
# 세조각 나누는 기준을 j와 k로 둠
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            p = str[:j][::-1] + str[j:k][::-1] + str[k:][::-1]
            li.append(p)
print(min(li))
