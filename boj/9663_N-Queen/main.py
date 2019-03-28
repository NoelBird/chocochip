# nq 함수만 있으면 전부 해결되지만, 약 2배정도의 속도 향상을 위하여 비슷한 함수를 복사 붙여넣기 했습니다.

buf1 = []
buf2 = []

def nq(l, idx, max_idx):
    global buf1
    global buf2
    if idx == max_idx:
        return 1
    if idx > max_idx:
        return 0
    ans = 0
    for i in range(len(l)):
        if idx+l[i] in buf1:
            continue
        if idx-l[i] in buf2:
            continue
        buf1 += [idx+l[i]]
        buf2 += [idx-l[i]]
        ans += nq(l[:i] + l[i+1:], idx+1, max_idx)
        del buf1[-1]
        del buf2[-1]
    return ans

def nq_odd1(l, idx, max_idx):
    global buf1
    global buf2
    if idx == max_idx:
        return 1
    if idx > max_idx:
        return 0
    ans = 0
    for i in range(len(l)//2):
        if idx+l[i] in buf1:
            continue
        if idx-l[i] in buf2:
            continue
        buf1 += [idx+l[i]]
        buf2 += [idx-l[i]]
        ans += nq(l[:i] + l[i+1:], idx+1, max_idx)
        del buf1[-1]
        del buf2[-1]
    return ans

def nq_odd2(l, idx, max_idx):
    global buf1
    global buf2
    if idx == max_idx:
        return 1
    if idx > max_idx:
        return 0
    ans = 0
    for i in range(len(l)//2, len(l)//2 + 1):
        if idx+l[i] in buf1:
            continue
        if idx-l[i] in buf2:
            continue
        buf1 += [idx+l[i]]
        buf2 += [idx-l[i]]
        ans += nq(l[:i] + l[i+1:], idx+1, max_idx)
        del buf1[-1]
        del buf2[-1]
    return ans

def nq_even(l, idx, max_idx):
    global buf1
    global buf2
    if idx == max_idx:
        return 1
    if idx > max_idx:
        return 0
    ans = 0
    for i in range(len(l)):
        if idx == 0 and i>= max_idx//2:
            break
        if idx+l[i] in buf1:
            continue
        if idx-l[i] in buf2:
            continue
        buf1 += [idx+l[i]]
        buf2 += [idx-l[i]]
        ans += nq(l[:i] + l[i+1:], idx+1, max_idx)
        del buf1[-1]
        del buf2[-1]
    return ans

n = int(input())

l = list(range(n))
if n%2 == 0:
    print(nq_even(l, 0, n)*2)
else:
    print(nq_odd1(l, 0, n)*2 + nq_odd2(l, 0, n))
