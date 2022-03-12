t = int(input())
ps_list = []
for i in range(t):
    ps_list.append(input())

for ps in ps_list:
    stack = list(ps)
    right_list = []
    left_list = []
    for _ in range(len(stack)):     
        last_one = stack.pop()
        if last_one == ')':
            right_list.append(last_one)
        else: 
            if len(right_list) > 0 :
                right_list.pop()
            else:
                left_list.append(last_one)
            
    if len(right_list) == 0 and len(left_list) == 0 :
        print('YES')
    else:
        print('NO')