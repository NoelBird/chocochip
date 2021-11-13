from itertools import combinations

def make_comb(l_honey, C):
    max_C = 0
    l = []
    for i in range(1, len(l_honey)+1):
        for j in combinations(l_honey, i):
            max_C_tmp = sum(j)
            if max_C_tmp == C:
                return j
            if max_C_tmp < C and max_C_tmp > max_C:
                max_C = max_C_tmp
                l = j
    return l

def find_max(map_honey, N, M, C):
    _max = 0
    for i_y1 in range(N):
        for i_x1 in range(N-M+1):    # 첫 번째 사람의 index
            l1 = make_comb(map_honey[i_y1][i_x1:i_x1+M], C)
            # for i_x2 in range(i_x1+M, N-M+1):
            #         l2 = make_comb(map_honey[i_y1][i_x2:i_x2+M], C)
            #         tmp = sum(map(lambda x: x**2, l1+l2))
            #         if tmp > _max:
            #             _max = tmp
            for i_y2 in range(i_y1+1, N):
                for i_x2 in range(N-M+1):
                    l2 = make_comb(map_honey[i_y2][i_x2:i_x2+M], C)
                    tmp = sum(map(lambda x: x**2, l1+l2))
                    if tmp > _max:
                        _max = tmp
    return _max

T = int(input())
for i in range(T):
    N, M, C = map(int, input(' ').split())  # M: 벌통의 개수, C: 꿀통의 사이즈
    map_honey = [list(map(int, input().split())) for _ in range(N)]
    print("#%d %d" % (i+1, find_max(map_honey, N, M, C)))