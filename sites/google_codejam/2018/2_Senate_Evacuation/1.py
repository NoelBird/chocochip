T = int(input())
for tc in range(1, T+1):
    N = int(input())
    l = list(map(int, input().split()))
    result = []
    while True:
        if sum(l) == 2:
            idx1 = l.index(1)
            l[idx1] -= 1
            idx2 = l.index(1)
            result.append(chr(idx1 + 0x41) + chr(idx2+0x41))
            break
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