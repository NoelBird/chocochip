def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)

def comb(n, m):
    return fac(n)//(fac(n-m)*fac(m))

def gen_l(l, l_ans, idx, max_idx):
    if len(l_ans) == max_idx +1:
        return l_ans
    if len(l_ans) > max_idx +1:
        return -1
    ans = -1

n = int(input())
if n >= 1024:
    print(-1)
else:
    ndigit = 1
    a = 0
    while True:
        tmp = comb(10, ndigit)
        if a + tmp >= n:
            break
        a += tmp
        ndigit += 1
    
    # print(gen_l(list(range(10)), [], 0, n))