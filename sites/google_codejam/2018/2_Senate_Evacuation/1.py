# 논리적으로 헷갈렸음
# 맨 마지막만 2명이 되면 그 때만 2명이 한꺼번에 빠지면 된다고 생각했는데,
# 정당 2개인 경우라면 항상 같이 빠져야 했음
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    l = list(map(int, input().split()))
    result = []
    while True:
        cnt = 0
        for i in range(len(l)):
            if l[i] != 0:
                cnt += 1
        if cnt == 2:
            idx1 = -1
            idx2 = -1
            for i in range(len(l)):
                if l[i] != 0:
                    if idx1 < 0:
                        idx1 = i
                    else:
                        idx2 = i
                        break
            if l[idx1] == l[idx2]:
                result.append(chr(idx1 + 0x41) + chr(idx2+0x41))
                l[idx1] -= 1
                l[idx2] -= 1
                continue
        if sum(l) == 0:
            break
        # find index of max value
        max_val = 0
        max_idx = -1
        for i in range(len(l)):
            if l[i] > max_val:
                max_val = l[i]
                max_idx = i
        result.append(chr(max_idx + 0x41))
        l[max_idx] -= 1
    result = " ".join(result)
    print(f"Case #{tc}: {result}")