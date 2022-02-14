from pprint import pprint
T = int(input())

for tc in range(1, T+1):
    if tc != 1:
        t = int(input())
    N, B, F = map(int, input().split())
    # no use of F

    # 1. make time-workers table
    # 2. 
    table = [[0]*16 for _ in range(4)]
    cnt = 0
    for i in range(len(table[0])):
        for j in range(len(table)):
            table[j][i] = bin(cnt)[2:].zfill(4)[j]
        cnt += 1
            
    groups = []
    for i in range(0, N, 16):
        if N - i >= 16:
            groups.append(16)
        else:
            groups.append(N-i)
    
    # make first query
    bad_workers = []
    if N > 16:
        q = ""
        is_odd = False
        for group in groups:
            if is_odd:
                q += "1"*group
            else:
                q += "0"*group
            is_odd = not is_odd
        print(q)

        # get first response
        s = input()
        state = "0"
        cnt_b = 0
        for i in range(len(s)):
            if s[i] == state:
                cnt_b += 1
            else:
                bad_workers.append(16 - cnt_b)
                cnt_b = 1
                state = s[i]
        if cnt_b != 0:
            bad_workers.append(16 - cnt_b)
        if len(bad_workers) != len(groups):
            bad_workers.append(groups[-1])
    else:
        bad_workers = [B]

    # make query
    ret_vals = []
    for i in range(len(table)):
        q = ""
        for group in groups:
            for j in range(group):
                q += table[i][j]
        print(q)
        s = input()
        ret_vals.append(s)
    
    # print(ret_vals)
    normal_workers = []
    for i in range(len(bad_workers)):
        num_normal_worker = groups[i] - bad_workers[i] if N > 16 else N-B
        cur_group = []
        for normal_worker in range(num_normal_worker):
            tmp = ""
            for i in range(len(ret_vals)):
                tmp += ret_vals[i][normal_worker]
            cur_group.append(int(tmp, 2))
        normal_workers.append(cur_group)
    # print(normal_workers)

    base = 0
    result = []
    for i in range(len(groups)):
        result += list(map(lambda x: x+base, sorted(list(set(list(range(groups[i]))) - set(normal_workers[i])))))
        base += 16
    print(" ".join(map(str,result)))

