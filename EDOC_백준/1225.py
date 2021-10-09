a, b= map(str,input().split())

a_list = a
b_list = b
result = 0
for i in a_list:
    for j in b_list:
        result+=int(i)*int(j)

print(result)