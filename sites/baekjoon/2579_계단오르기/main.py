T = int(input())

# 입력받기
l = []
for _ in range(T):
    l.append(int(input()))
len_l = len(l)
# 계산
cache = {}
def dp(idx, cnt):
    global l
    global len_l
    global cache

    # cache에 있는 경우
    if cache.get((idx, cnt)):
        return cache[(idx, cnt)]
    
    # 종료조건 - 성공
    if idx <= 0:
        ret = l[0]
    elif (idx == 1 and cnt == 2):
        ret = l[1]
    else:
        if cnt == 1:
            ret1 = dp(idx -1, 2)
            ret2 = dp(idx -2, 1)
            ret = max(ret1, ret2) + l[idx]
        else:
            ret = dp(idx -2, 1) + l[idx]
    cache[(idx, cnt)] = ret
    return ret

print(dp(len_l - 1, 1))