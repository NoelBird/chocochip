# 입력 부분
def myreplace(s):
    ans = []
    for i in range(len(s)):
        if s[i] == '0':
            ans.append(' ')
        else:
            ans.append('#')
    return ''.join(ans)

def solution(n, arr1, arr2):
    l = []
    for item in zip(arr1, arr2): # ( 9 | 30 )
        a = item[0] | item[1] # 31
        an = '{:b}'.format(a).zfill(n) # '11111'
        b = myreplace(an) # '#####'
        l.append(b)

    return l