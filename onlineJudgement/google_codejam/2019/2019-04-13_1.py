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
        print(idx, l[i])
        ans += nq(l[:i] + l[i+1:], idx+1, max_idx)
        del buf1[-1]
        del buf2[-1]
    return ans

T = int(input())
for i in range(T):
    ans = nq()
n = int(input())

l = list(range(n))
ans = nq(l, 0, n)
if ans == 0:


