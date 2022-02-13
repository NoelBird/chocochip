T = int(input())

def calc_op(l):
    cnt = 0
    for i in range(len(l)):
        if l[i] % 2 == 0:
            cnt += l[i]//2
        else:
            cnt += l[i]//2+1
    return cnt

for _ in range(T):
    N = int(input())
    l = list(map(int, input().split()))[1:-1]
    if len(l) == 1:
        if l[0]%2 == 0:
            print(calc_op(l))
        else:
            print(-1)
    else:
        is_2_over_exists = False
        for i in l:
            if i >= 2:
                is_2_over_exists = True
                break
        if is_2_over_exists:
            print(calc_op(l))
        else:
            print(-1)
