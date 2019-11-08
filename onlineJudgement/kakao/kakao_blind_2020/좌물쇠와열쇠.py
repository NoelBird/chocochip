def rotate90(key):
    N = len(key)
    l = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            l[j][N-1-i] = key[i][j]
    return l

def add_padding(lock, LEN_LOCK, LEN_KEY, LEN_TOT):
    l = [[0]*LEN_TOT for _ in range(LEN_KEY)]
    for i in range(LEN_LOCK):
        l.append([0]*LEN_KEY + lock[i] + [0]*LEN_KEY)
    l += [[0]*LEN_TOT for _ in range(LEN_KEY)]
    return l

def solution(key, lock):
    LEN_KEY = len(key)
    LEN_LOCK = len(lock)
    LEN_TOT = 2*LEN_KEY+LEN_LOCK

    # 패딩 주기
    l = add_padding(lock, LEN_LOCK, LEN_KEY, LEN_TOT)

    # 90도 회전 4번하고, 전체 탐색하기
    for _ in range(4):
        key = rotate90(key)
        for i in range(LEN_KEY+LEN_LOCK):
            for j in range(LEN_KEY+LEN_LOCK):
                # key 확인
                isCorrect = True
                l_tmp = [[l[k][p] for p in range(LEN_TOT)] for k in range(LEN_TOT)]
                for k in range(LEN_KEY):
                    for p in range(LEN_KEY):
                        cur_y = i+k
                        cur_x = j+p
                        if not(LEN_KEY <= cur_y < LEN_KEY+LEN_LOCK):
                            continue
                        if not(LEN_KEY <= cur_x < LEN_KEY+LEN_LOCK):
                            continue
                        if l[cur_y][cur_x] == key[k][p]:
                            isCorrect = False
                            break
                        l_tmp[cur_y][cur_x] = 1
                    if not isCorrect:
                        break
                if not isCorrect:
                    continue

                # 잘 됐는지 체크
                isAns = True
                for k in range(LEN_KEY, LEN_KEY + LEN_LOCK):
                    for p in range(LEN_KEY, LEN_KEY + LEN_LOCK):
                        if l_tmp[k][p] == 0:
                            isAns = False
                            break
                    if not isAns:
                        break
                if isAns:
                    return True

    answer = False
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))