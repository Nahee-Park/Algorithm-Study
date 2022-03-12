N = int(input())
word_list = []

for i in range(N):
    word_list.append(input())
    
result = 0

for idx in range(1,N):
    base_word = list(word_list[0])
    check_word = list(word_list[idx])
    for _ in word_list[idx]:
        s = check_word.pop(0)
        # base_word에 있으면 지우기
        # 없으면 check에 남겨두기 
        if s in base_word:
            base_word.remove(s)
        else:
            check_word.append(s)
    # base엔 최대 1개 넘게 남아있으면 안됨
    # check에 남아있는 것도 최대 ㅎ1개 넘게 남아있으면 안됨
    A = len(base_word)
    B = len(check_word)
    if (A==0 and B==0) or (A==1 and B==1) or (A==1 and B==0) or (A==0 and B==1):
        result += 1

print(result)
