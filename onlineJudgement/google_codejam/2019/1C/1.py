import sys
input = sys.stdin.readline

from collections import defaultdict

T = int(input().strip())
for i in range(T):
    A = int(input().strip())
    C = defaultdict(list)
    len_C = []
    C_live = [True for _ in range(A)]
    for j in range(A):
        C[j] = list(input().strip())
        len_C.append(len(C[j]))
    
    ans = ''
    for j in range(500):
        cur = set()
        Rs = []
        Ss = []
        Ps = []
        for k in range(A):
            if not C_live[k]:
                continue
            tmp = C[k][j % len_C[k]]
            cur.update(tmp)
            if tmp == 'R':
                Rs.append(k)
            elif tmp == 'S':
                Ss.append(k)
            elif tmp == 'P':
                Ps.append(k)
        if cur == {'R', 'S', 'P'}:
            print("Case #%d: IMPOSSIBLE" % (i+1))
            break
        elif cur == {'R', 'S'}:
            ans += 'R'
            for k in range(len(Ss)):
                C_live[Ss[k]] = False
        elif cur == {'S', 'P'}:
            ans += 'S'
            for k in range(len(Ps)):
                C_live[Ps[k]] = False
        elif cur == {'P', 'R'}:
            ans += 'P'
            for k in range(len(Rs)):
                C_live[Rs[k]] = False
        elif cur == {'R'}:
            ans += 'P'
            print("Case #%d: %s" % (i+1, ans))
            break
        elif cur == {'S'}:
            ans += 'R'
            print("Case #%d: %s" % (i+1, ans))
            break
        elif cur == {'P'}:
            ans += 'S'
            print("Case #%d: %s" % (i+1, ans))
            break
    else:
        print("Case #%d: IMPOSSIBLE" % (i+1))