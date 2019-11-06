from collections import defaultdict

T = int(input())

def possible_test(R, C):
    l = [(2, 2), (2, 3), (2, 4), (3, 3)]
    if (R, C) in l:
        return False
    else:
        return True

def case2(R, C, isSame):
    for i in range(1, C+1): # x
        for j in range(1, R+1): # y
            if isSame:
                cur_x = i if j%2 == 1 else (i+3-1)%C+1
                cur_y = j
            else:
                cur_y = i if j%2 == 1 else (i+3-1)%C+1
                cur_x = j
            print("%d %d" % (cur_y, cur_x))

def caseElse(R, C, isSmae):
    for i in range(1, C+1):
        if i != C:
            for j in range(1, R+1):
                if isSame:
                    cur_x = i if j%2 == 1 else (i+2-1)%C+1
                    cur_y = j
                else:
                    cur_y = i if j%2 == 1 else (i+2-1)%C+1
                    cur_x = j
                print("%d %d" % (cur_y, cur_x))
        else:
            l = []
            for j in range(1, R+1):
                if isSame:
                    cur_x = i if j%2 == 1 else (i+2-1)%C+1
                    cur_y = j
                else:
                    cur_y = i if j%2 == 1 else (i+2-1)%C+1
                    cur_x = j
                l.append([cur_x, cur_y])
            l = l[1:] + [l[0]]
            for j in l:
                print("%d %d" % (j[1], j[0]))

for i in range(T):
    R, C = map(int, input().split())
    x1, x2 = sorted([R, C])
    isSame = True if R == x1 and C == x2 else False
    isPossible = possible_test(x1, x2)
    if not isPossible:
        print("Case #%d: IMPOSSIBLE" % (i+1))
        continue
    else:
        print("Case #%d: POSSIBLE" % (i+1))
        if x1 == 2:
            case2(x1, x2, isSame)
        else:
            caseElse(x1, x2, isSame)
