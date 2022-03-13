password = list(map(int,input()))
dp = [0] * (len(password)+1)

if password[0] == 0:
    print('0')
else:
    password = [0] + password
    dp[0]=dp[1]=1
    for i in range(2,len(password)):
        # 그냥 한자리만 가능하면 이전 dp값 가져옴 
        if password[i] > 0 :
            dp[i] += dp[i-1]
        # 두자리가 가능한 수이면 그 이전 dp값까지 누적시킴
        temp = password[i-1] * 10 + password[i]
        if temp >= 10 and temp <= 26:
            dp[i] += dp[i-2]
    print(dp.pop() % 1000000)