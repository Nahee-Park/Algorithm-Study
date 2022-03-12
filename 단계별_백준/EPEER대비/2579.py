N = int(input())
step_list = []
for _ in range(N):
    step_list.append(int(input()))
    
if len(step_list) == 1 :
    print(step_list[0])
elif len(step_list) ==2 :
    print(sum(step_list))
else:    
    dp = []
    dp.append(step_list[0])
    dp.append(max(step_list[0] + step_list[1], step_list[1]))
    dp.append(max(step_list[1] + step_list[2],step_list[0]+step_list[2]))
    for i in range(3,N):
        # 한 칸 띄어서 더하거나 , 이어서 더할 거면 dp에선 아예 더 띄어져 있는 애를 선택해서 비교
        dp.append(max(dp[i-2] + step_list[i],dp[i-3]+step_list[i]+step_list[i-1]))

    print(dp.pop())