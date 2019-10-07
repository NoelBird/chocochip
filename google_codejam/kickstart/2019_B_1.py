from collections import Counter

# 2
# 7 5
# ABAACCA
# 3 6
# 4 4
# 2 5
# 6 7
# 3 7
# 3 5
# XYZ
# 1 3
# 1 3
# 1 3
# 1 3
# 1 3

# Case #1: 3
# Case #2: 0


T = int(input())
for i in range(T):
    N, Q = map(int, input().split())
    l = list(input())
    p_cnt = 0
    for j in range(Q):
        L, R = map(int, input().split())
        L -= 1 # index로 만들기
        R -= 1

        cnt = Counter(l[L:R+1])
        if (L+R) % 2 == 0: # 아이템이 홀 수 개인 경우
            isP_cnt = 0
            for k in cnt:
                if cnt[k]%2 != 0:
                    isP_cnt += 1
                    if isP_cnt >= 2:
                        break
            if isP_cnt < 2:
                p_cnt += 1
        else:
            isP_cnt = 0
            for k in cnt:
                if cnt[k]%2 != 0:
                    isP_cnt += 1
                    break
            if not isP_cnt:
                p_cnt += 1
    print("Case #%d: %d" % (i+1, p_cnt))
