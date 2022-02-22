# 1. find optimal binary values
# 2. make an order-index(by 1 0 difference desc)
# 3. increase a number 1 to K and apply order-index here
# 4. xor to optimal binary values
# 5. check if exists in impossible binaries

from audioop import reverse


T = int(input())
for tc in range(1, T+1):
    # num of lines, num of impossible, len of binary
    N, M, P = map(int, input().split())
    mat = []
    for i in range(N):
        mat.append(list(map(int, list(input()))))
    
    base = []
    base_bin = []
    diff = []
    diff_bin = []
    for i in range(P):
        cnt = 0
        for j in range(N):
            cnt += mat[j][i]
        base.append(cnt)
        if cnt >= (N+1)//2:
            base_bin.append(1)
        else:
            base_bin.append(0)
        diff_bin.append([cnt, N-cnt])
        diff.append(N - cnt)
    diff_idx = [(i, a) for i, a in enumerate(diff)]
    diff_idx.sort(key=lambda x:x[1], reverse=True)
    diff_idx = [i[0] for i in diff_idx]
    
    impossibles = []
    for i in range(M):
        impossibles.append(list(map(int, list(input()))))
    
    result = 0
    for i in range(0, M+1):
        tmp = list(map(int, list(bin(i)[2:].zfill(P))))
        tmp2 = [tmp[i] for i in diff_idx]
        new_bin = [0]*P
        result = 0
        for j in range(P):
            new_bin[j] = tmp2[j]^base_bin[j]
            result += diff_bin[j][new_bin[j]]
        # print(result)
        if new_bin in impossibles:
            continue
        else:
            break
        
    
    print(f"Case #{tc}: {result}")