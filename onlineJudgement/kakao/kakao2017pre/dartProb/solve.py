l = [0]
def expChar(idx, c):
    global l
    if c == 'S':
        return
    elif c == 'D':
        l[idx] = l[idx]**2
        return
    else:
        l[idx] = l[idx]**3
        return

def special(idx, c):
    global l
    if c == '*':
        l[idx] *= 2
        l[idx-1] *= 2
    else:
        l[idx] *= -1

def solution(dartResult):
    dartResult += ' '
    global l
    l = [0]
    idx = 0

    for i in range(len(dartResult)-1):
        if dartResult[i].isdigit(): # 10때문에 문제가 생김
            if dartResult[i+1].isdigit():
                continue
            if dartResult[i-1].isdigit():
                l.append(int(dartResult[i-1:i+1]))
                idx += 1
                continue
            l.append(int(dartResult[i]))
            idx += 1
        elif dartResult[i].isalpha():
            expChar(idx, dartResult[i])
        else:
            special(idx, dartResult[i])

    answer = sum(l)
    return answer