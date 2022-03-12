n = int(input())
p = list(map(int,input().split()))
sorted_p = sorted(p)
result = 0
for idx in range(len(sorted_p)):
    result += sorted_p[idx] * (len(sorted_p) -idx)
print(result)