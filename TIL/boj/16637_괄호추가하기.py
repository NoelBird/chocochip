# 9
# 3+8*7-9*2

MIN_VAL = -2**32

buf = []


def make_calc(s):
    if len(s) <= 1:
        return eval(s)
    if s[0] == '-':
        if s[3] == '-':
            return make_calc(str(eval(s[0:5])) + s[5:])
        else:
            return make_calc(str(eval(s[0:4])) + s[4:])
    else:
        if s[2] == '-':
            return make_calc(str(eval(s[0:4])) + s[4:])
        else:
            return make_calc(str(eval(s[0:3])) + s[3:])


def dfs(s_before_processing, s_after_processing):
    if not s_before_processing:
        return make_calc(s_after_processing)

    # if there is a bracket
    cur_s = s_before_processing[:3]
    m1 = dfs(s_before_processing[4:], s_after_processing + (str(eval(cur_s))) + s_before_processing[3:4])
    # if there is no bracket
    m2 = dfs(s_before_processing[2:], s_after_processing + s_before_processing[:2])
    return max(m1, m2)


N = int(input())
l = input()
ans = dfs(l, "")
print(ans)
