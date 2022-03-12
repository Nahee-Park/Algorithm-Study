N = int(input())
is_result = False
    
for i in range(1,N):
    i_len = len(str(i))
    i_list = []
    for j in range(i_len):
        i_list.append(int(str(i)[j]))
    if sum(i_list) + int(i) == N :
        print(int(i))
        is_result = True
        break
if is_result==False:
    print(0)