def solution(s):
    N = len(s)
    min_ans = 1000
    for i in range(1, N//2+1):
        tmp = s[0:i]
        l = []
        cnt = 1
        cur_ans = 0
        for j in range(i, N, i): # step is i
            tmp2 = s[j:j+i]
            if tmp == tmp2: # 같은 경우에는 count++, 
                cnt += 1
            else: # 같지 않은 경우에는 cur_ans에 추가
                if cnt == 1:
                    cur_ans += len(tmp)
                else:
                    cur_ans += len(str(cnt)) + len(tmp)
                tmp = tmp2
                cnt = 1
        if cnt == 1:
            cur_ans += len(tmp)
        else:
            cur_ans += len(str(cnt)) + len(tmp)
        min_ans = min(min_ans, cur_ans)
    answer = min_ans
    return answer

print(solution("a"))